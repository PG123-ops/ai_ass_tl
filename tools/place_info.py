import requests

def get_place_info(place: str):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{place}"
    headers = {
        "User-Agent": "ai_ops_assistant/1.0 (puspendug@gmail.com)"  
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
