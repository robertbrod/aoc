import requests

USER_AGENT = "https://github.com/robertbrod/aoc by robbrod93@gmail.com"

def fetch_input(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {
        "User-Agent": USER_AGENT,
        "Cookie": "session=53616c7465645f5f5d900372593ad46d8945b3d65439e0ce7ff4a66f760fea4f2de1a91fe0a3d5ba8b24d3b934b13b225287c1a2f1756dfb2a82f3799d1f6c80"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data_array = response.text.split("\n")
        return data_array
    else:
        raise Exception(f"AoC endpoint request failed. Status code: {response.status_code}")