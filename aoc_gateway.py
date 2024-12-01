import requests
import os
import config_manager
from datetime import datetime
from bs4 import BeautifulSoup

def fetch_input(year, day):
    if os.path.exists(f"{year}/{day}/{year}_{day}_input.txt"):
        raise Exception(f"Input data for day {day} ({year}) already cached.")
    
    if minutes_since_last_outbound_call() < int(config_manager.get_state("outbound_api_call_throttle")):
        raise Exception(f"Cancelling AoC endpoint request; the last request was too recent.")
    
    url = f"https://adventofcode.com/{year}/day/{day}/input"

    response = requests.get(url, headers = fetch_headers())
    
    config_manager.update_last_outbound_api_call_time()

    if response.status_code == 200:
        data = response.text
        return data
    else:
        raise Exception(f"AoC endpoint request failed. Status code: {response.status_code}")
    
def submit_answer(year, day, part, answer):
    print(f"Submiting answer ({answer}) for day {day} - part {part} puzzle ({year})")
    
    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    payload = {
        "level": part,
        "answer": answer
    }
    
    response = requests.post(url, headers = fetch_headers(), data = payload)
    
    if response.status_code == 200:
        data = response.text
        return parse_answer_response(data)
    else:
        raise Exception(f"AoC endpoint request failed. Status code: {response.status_code}")
    
def minutes_since_last_outbound_call():
    last_call_str = config_manager.get_state("last_outbound_api_call_time")
    last_call = datetime.fromisoformat(last_call_str)
    current_time = datetime.now()
    time_difference = current_time - last_call
    return time_difference.total_seconds() / 60

def fetch_headers():
    return {
        "User-Agent": config_manager.get_state("user_data")["user_agent"],
        "Cookie": os.getenv("AOC_COOKIE")
    }
    
def parse_answer_response(response):
    soup = BeautifulSoup(response, 'html.parser')
    
    article = soup.find('article')
    paragraph = article.find('p')
    result = paragraph.get_text()
    
    if "Did you already complete it?" in result:
        result = "Puzzle already completed!"
    elif "That's the right answer!" in result:
        result = "Correct answer!"
        
    return result