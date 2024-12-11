import requests
import os
import config_manager
import util
from models import Participant
from datetime import datetime
from bs4 import BeautifulSoup
from exceptions import DataAlreadyCached
from exceptions import APIRequestThrottled

@staticmethod
def fetch_input(year: str, day: str) -> str:
    """
    Writes puzzle input data to disk. Saves to `year/day/year_day_input.txt`

    Args:
        data (str): response from AoC API request
        year (str): puzzle year
        day (str): puzzle day

    Returns:
        Response from AoC API

    Raises:
        DataAlreadyCached
            If the input data has already been cached on disk, we do not want to make an API call
            
        APIRequestThrottled
            If we have made an API request for puzzle input too recently, we do not want to make an API call.
            This throttle value is set in `config.json` 
            
        HTTPError
            We got a 4xx or 5xx response from AoC API
    """
    
    print(f"Fetching input data for day {day} ({year})...")
    
    if os.path.exists(f"{year}/{day}/{year}_{day}_input.txt"):
        raise DataAlreadyCached(f"Input data for day {day} ({year}) already cached.")
    
    if _minutes_since_last_outbound_call() < int(config_manager.get_config("outbound_api_call_throttle")):
        raise APIRequestThrottled(f"Cancelling AoC endpoint request; the last request was too recent.")
    
    url = f"https://adventofcode.com/{year}/day/{day}/input"

    response = requests.get(url, headers = _fetch_headers())
    
    config_manager.update_last_outbound_api_call_time()

    if response.status_code == 200: 
        data = response.text
        print(f"Finished fetching input data for day {day} ({year}).")
        return data
    else:
        response.raise_for_status()
    
def submit_answer(year: str, day: str, part: str, answer: int) -> str:
    """
    Submits puzzle answer to AoC

    Args:
        year (str): puzzle year
        day (str): puzzle day
        part (str): puzzle part (1 or 2)
        asnwer (int): puzzle solution

    Returns:
        Response from AoC API

    Raises:
        HTTPError
            We got a 4xx or 5xx response from AoC API
    """
    
    print(f"Submiting answer for day {day} - part {part} puzzle ({year})...")
    
    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    payload = {
        "level": part,
        "answer": answer
    }
    
    response = requests.post(url, headers = _fetch_headers(), data = payload)
    
    if response.status_code == 200:
        data = response.text
        print(f"Finished submiting answer for day {day} - part {part} puzzle ({year})...")
        return _parse_answer_response(data)
    else:
        response.raise_for_status()
    
def fetch_leaderboard() -> list[Participant]:
    """
    Fetches participant data from private leaderboard

    Args:
        None

    Returns:
        List of participants in private leaderboard. This model holds participant name, leaderboard position, and number of stars

    Raises:
        HTTPError
            We got a 4xx or 5xx response from AoC API
    """
    
    if _minutes_since_last_leaderboard_call() < int(config_manager.get_config("leaderboard_api_throttle")):
        return util.fetch_leaderboard()
    
    print(f"Refreshing private leaderboard stats...")
    
    response = requests.get(config_manager.get_config("private_leaderboard_url"), headers = _fetch_headers())
    
    config_manager.update_last_leaderboard_api_call_time()
    
    if response.status_code == 200:
        participants = []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        priv_board_rows = soup.find_all(class_ = 'privboard-row')
        priv_board_rows = priv_board_rows[1:]
        
        for row in priv_board_rows:
            participant = Participant()
            
            # Parse the participant's name
            name_div = row.find(class_ = 'privboard-name')
            if name_div:
                name_text = name_div.get_text()
                if '(AoC++)' in name_text:
                    name_text = name_text.replace(' (AoC++)', '')
                participant.name = name_text
            
            # Parse the participant's number of stars
            two_star_divs = row.find_all(class_ = 'privboard-star-both')
            one_star_divs = row.find_all(class_ = 'privboard-star-firstonly')
            
            total_stars = 0
            
            if two_star_divs:
                total_stars += 2 * len(two_star_divs)
                
            if one_star_divs:
                total_stars += len(one_star_divs)
            
            participant.stars = total_stars
            
            # Parse the participant's leaderboard position
            position = None
  
            position_div = row.find(class_ = 'privboard-position')
            if position_div and participant.stars > 0:
                position_text = position_div.get_text()
                position_text = position_text.replace(')', '')
                
                position = int(position_text)
                
            participant.position = position
            
            participants.append(participant)
            
        util.cache_leaderboard(participants)
        return participants
            
    else:
        response.raise_for_status()
    
# ---------- Internal Functions ----------
 
def _minutes_since_last_outbound_call():
    last_call_str = config_manager.get_config("last_outbound_api_call_time")
    last_call = datetime.fromisoformat(last_call_str)
    current_time = datetime.now()
    time_difference = current_time - last_call
    return time_difference.total_seconds() / 60

def _minutes_since_last_leaderboard_call():
    last_call_str = config_manager.get_config("last_leaderboard_api_call_time")
    last_call = datetime.fromisoformat(last_call_str)
    current_time = datetime.now()
    time_difference = current_time - last_call
    return time_difference.total_seconds() / 60

def _fetch_headers():
    return {
        "User-Agent": config_manager.get_config("user_data")["user_agent"],
        "Cookie": os.getenv("AOC_COOKIE")
    }
    
def _parse_answer_response(response):
    soup = BeautifulSoup(response, 'html.parser')
    
    article = soup.find('article')
    paragraph = article.find('p')
    result = paragraph.get_text()
    
    if "Did you already complete it?" in result:
        result = "Puzzle already completed!"
    elif "That's the right answer!" in result:
        result = "Correct answer!"
    elif "That's not the right answer." in result:
        result = "Wrong answer!"
    elif "your answer is too high" in result:
        result = "Submitted answer is ABOVE the expected answer."
    elif "your answer is too low" in result:
        result = "Submitted answer is BELOW the expected answer."
    elif "You gave an answer too recently" in result:
        sentences = result.split(".")
        time_statement = sentences[1].split()
        result = (f"You must wait {time_statement[2]} {time_statement[3]}...")
        
    return result