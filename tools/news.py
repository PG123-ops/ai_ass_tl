import requests
import os

def get_news(topic=None, country="in"):
    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "apiKey": os.getenv("NEWS_API_KEY"),
        "country": country
    }

    if topic:
        params["q"] = topic

    response = requests.get(url, params=params)
    response.raise_for_status()

    articles = response.json().get("articles", [])[:5]

    return [
        {
            "title": article["title"],
            "source": article["source"]["name"]
        }
        for article in articles
    ]
