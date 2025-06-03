import requests

def run_username_scan(username):
    platforms = {
        "Twitter": f"https://twitter.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "OnlyFans": f"https://onlyfans.com/{username}",
        "Pornhub": f"https://www.pornhub.com/users/{username}",
        "OKCupid": f"https://www.okcupid.com/profile/{username}",
        "Last.fm": f"https://www.last.fm/user/{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "FurAffinity": f"https://www.furaffinity.net/user/{username}/",
    }

    results = {}
    for site, url in platforms.items():
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                results[site] = {"url": url, "exists": True}
            elif r.status_code == 404:
                results[site] = {"url": url, "exists": False}
            else:
                results[site] = {"url": url, "status": r.status_code}
        except:
            results[site] = {"url": url, "error": "timeout or blocked"}

    return results
from modules.utils import search_google

google_html = search_google(f"site:linkedin.com/in {username}")


