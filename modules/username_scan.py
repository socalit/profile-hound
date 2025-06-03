import requests

def run_username_scan(username):
    platforms = {
        "Twitter": f"https://twitter.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "TikTok": f"https://www.tiktok.com/@{username}"
    }

    results = {}
    for name, url in platforms.items():
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                results[name] = {"url": url, "exists": True}
            elif r.status_code == 404:
                results[name] = {"url": url, "exists": False}
            else:
                results[name] = {"url": url, "status": r.status_code}
        except:
            results[name] = {"url": url, "error": "timeout or blocked"}
    return results
