from tools.weather import get_weather
from tools.github import get_repo_stats
from tools.news import get_news
from tools.place_info import get_place_info

def execute_step(step):
    tool = step["tool"]
    action = step["action"]
    params = step["params"]

    if tool == "weather":
        return get_weather(params["city"])

    if tool == "github":
        return get_repo_stats(params["owner"], params["repo"])

    if tool == "news":
        return get_news(
            topic=params.get("topic"),
            country=params.get("country", "in")
        )

    if tool == "wiki":
        return get_place_info(params["place"])

    return {"error": f"Unknown tool: {tool}"}
