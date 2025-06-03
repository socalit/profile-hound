def run_address_enrichment(email=None, phone=None):
    person = {
        "full_name": None,
        "dob": None,
        "address": None,
        "relatives": [],
        "sources": []
    }

    person["note"] = "Address enrichment module is currently a stub. Implement with real source."

    if email:
        person["sources"].append(f"Searched by email: {email}")
    if phone:
        person["sources"].append(f"Searched by phone: {phone}")

    return person
