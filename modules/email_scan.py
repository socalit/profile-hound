import requests

def run_email_scan(email):
    result = {
        "email": email,
        "breaches": [],
    }

    api_key = "YOUR_HIBP_API_KEY"
    headers = {
        "hibp-api-key": api_key,
        "User-Agent": "profile-hound"
    }

    try:
        response = requests.get(
            f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            result["breaches"] = response.json()
        elif response.status_code == 404:
            result["breaches"] = []
        else:
            result["error"] = f"API error: {response.status_code}"
    except Exception as e:
        result["error"] = str(e)
    return result
