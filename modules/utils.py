import requests
from urllib.parse import quote

def search_google(query):
    """
    Performs a basic Google search and returns the raw HTML of the results page.
    This can be parsed later to extract URLs for LinkedIn, Facebook, etc.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; profile-hound/1.0; +https://github.com/socalit/profile-hound)"
    }

    try:
        encoded_query = quote(query)
        url = f"https://www.google.com/search?q={encoded_query}"
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.text  # HTML, to be parsed with regex or BeautifulSoup
        else:
            return f"[ERROR] Google returned status code {response.status_code}"
    except Exception as e:
        return f"[ERROR] Google search failed: {e}"
