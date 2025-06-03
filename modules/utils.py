from urllib.parse import quote
import requests
from bs4 import BeautifulSoup

def search_google(query, max_links=5):
    """
    Performs a Google search and extracts result URLs using BeautifulSoup.
    Returns a list of clean links (e.g., LinkedIn, Facebook).
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; profile-hound/1.0; +https://github.com/socalit/profile-hound)"
    }

    try:
        encoded_query = quote(query)
        url = f"https://www.google.com/search?q={encoded_query}&num={max_links}"
        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code != 200:
            return [f"[ERROR] Google returned status code {response.status_code}"]

        soup = BeautifulSoup(response.text, "html.parser")
        links = []

        for a_tag in soup.find_all("a"):
            href = a_tag.get("href")
            if href and "/url?q=" in href:
                cleaned = href.split("/url?q=")[1].split("&")[0]
                if "webcache.googleusercontent.com" not in cleaned:
                    links.append(cleaned)
            if len(links) >= max_links:
                break

        return links if links else ["[INFO] No links found."]
    except Exception as e:
        return [f"[ERROR] Google search failed: {e}"]
