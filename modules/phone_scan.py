import requests

def run_phone_scan(phone_number):
    result = {
        "phone": phone_number,
        "valid": False,
        "carrier": None,
        "location": None,
        "line_type": None
    }

    api_key = "YOUR_NUMVERIFY_API_KEY"
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}"

    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            result.update({
                "valid": data.get("valid"),
                "carrier": data.get("carrier"),
                "location": data.get("location"),
                "line_type": data.get("line_type")
            })
        else:
            result["error"] = f"API error: {r.status_code}"
    except Exception as e:
        result["error"] = str(e)
    return result
