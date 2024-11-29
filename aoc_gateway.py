import requests
import os
import state_manager
from datetime import datetime
from bs4 import BeautifulSoup

USER_AGENT = state_manager.get_state("user_data")["user_agent"]
THROTTLE = state_manager.get_state("outbound_api_call_throttle")
COOKIE = os.getenv("AOC_COOKIE")

def fetch_input(year, day):
    if minutes_since_last_outbound_call() < int(THROTTLE):
        raise Exception(f"Cancelling AoC endpoint request; the last request was too recent.")
    
    if os.path.exists(f"{year}/{day}/{year}_{day}_input.txt"):
        raise Exception(f"Cancelling AoC endpoint request; input data already cached.")

    url = f"https://adventofcode.com/{year}/day/{day}/input"

    response = requests.get(url, headers = fetch_headers())
    
    state_manager.update_last_outbound_api_call_time()

    if response.status_code == 200:
        data = response.text
        return data
    else:
        raise Exception(f"AoC endpoint request failed. Status code: {response.status_code}")
    
def submit_answer(year, day, part, answer):
    print(f"Submiting answer ({answer}) for {year} puzzle: day {day} part {part}")
    
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
    last_call_str = state_manager.get_state("last_outbound_api_call_time")
    last_call = datetime.fromisoformat(last_call_str)
    current_time = datetime.now()
    time_difference = current_time - last_call
    return time_difference.total_seconds() / 60

def fetch_headers():
    return {
        "User-Agent": USER_AGENT,
        "Cookie": COOKIE
    }
    
def parse_answer_response(response):
    soup = BeautifulSoup(response, 'html.parser')
    
    article = soup.find('article')
    paragraph = article.find('p')
    result = paragraph.get_text()
    
    if "Did you already complete it?" in result:
        result = "Puzzle already completed!"
        
    return result