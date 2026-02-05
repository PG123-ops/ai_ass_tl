import requests

def get_repo_stats(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    r = requests.get(url)
    r.raise_for_status()

    data = r.json()
    return {
        "repo": f"{owner}/{repo}",
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "open_issues": data["open_issues_count"]
    }
