import json
from pathlib import Path
from datetime import datetime

STATE_FILE = Path("aoc_state.json")

def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE, "r") as file:
            return json.load(file)
        
    return {}

def save_state(data):
    with open(STATE_FILE, "w") as file:
        json.dump(data, file, indent = 4)
        
def get_state(key):
    state = load_state()
    return state.get(key)

def set_state(key, value):
    state = load_state()
    state[key] = value
    save_state(state)
    
def update_last_outbound_api_call_time():
    set_state("last_outbound_api_call_time", datetime.now().isoformat())