#!/usr/bin/env python3
import argparse
import os
import json
from modules.username_scan import run_username_scan
from modules.email_scan import run_email_scan
from modules.phone_scan import run_phone_scan
from modules.address_enrichment import run_address_enrichment

RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

def save_results(target, data):
    output_file = os.path.join(RESULTS_DIR, f"{target}.json")
    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[+] Results saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="🕵️‍♂️ profile-hound: OSINT profiler for usernames, phones, and emails")
    parser.add_argument("--username", help="Username to scan")
    parser.add_argument("--email", help="Email address to scan")
    parser.add_argument("--phone", help="Phone number to scan")
    parser.add_argument("--all", action="store_true", help="Run all scans if data available")
    parser.add_argument("--output", choices=["json", "pretty"], default="pretty", help="Output format")

    args = parser.parse_args()
    collected_data = {}

    if args.all or args.username:
        if args.username:
            print(f"[*] Scanning username: {args.username}")
            collected_data["username"] = run_username_scan(args.username)

    if args.all or args.email:
        if args.email:
            print(f"[*] Scanning email: {args.email}")
            collected_data["email"] = run_email_scan(args.email)

    if args.all or args.phone:
        if args.phone:
            print(f"[*] Scanning phone: {args.phone}")
            collected_data["phone"] = run_phone_scan(args.phone)

    if "email" in collected_data or "phone" in collected_data:
        print("[*] Enriching address/profile info...")
        collected_data["person"] = run_address_enrichment(
            email=args.email,
            phone=args.phone
        )

    if collected_data:
        target_id = args.username or args.email or args.phone or "profile"
        save_results(target_id, collected_data)
    else:
        print("[-] No input provided. Use --username, --email, or --phone")

if __name__ == "__main__":
    main()

