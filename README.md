# profile-hound

`profile-hound` is a modular Python-based CLI OSINT tool that scans for usernames, phone numbers, and emails across social media, dating sites, public directories, and breach databases. It provides automatic link extraction from search engines and supports snapshot profiling.

Built by [socalit](https://github.com/socalit) for ethical recon, hotel auditing, and cyber investigations.

---

## Features

-  Checks username presence on 15+ platforms (social, music, adult, gaming)
-  Fallback search using Google for LinkedIn, Facebook, etc.
-  Email breach checks via HaveIBeenPwned
-  Phone validation + carrier/location via Numverify
-  Stub: Full name, DOB, address & relatives enrichment
-  `--output pretty` prints clean profile summary to terminal
-  JSON export to `results/` folder

---

## Installation

```bash
git clone https://github.com/socalit/profile-hound.git
cd profile-hound
chmod +x install-profile-hound.sh
./install-profile-hound.sh
```

You’ll be prompted to install headless browser tools if desired (Playwright/Selenium).

---

## Example Usage

```bash
# Scan by username only
python3 profile_hound.py --username johndoe

# Include email & phone metadata
python3 profile_hound.py --email test@example.com --phone +15551234567

# Full profile
python3 profile_hound.py --username johndoe --email test@example.com --phone +15551234567 --all

# Save output as JSON
python3 profile_hound.py --username johndoe --output json
```

---

## Platforms Scanned

| Category     | Examples |
|--------------|----------|
| Social Media | Twitter, Instagram, Reddit, GitHub, TikTok |
| Music/Forums | Last.fm, SoundCloud, DeviantArt, Steam |
| Adult/Dating | OnlyFans, Pornhub, OKCupid, FurAffinity |
| Fallback via Google | LinkedIn, Facebook |

---

## Output

- `results/USERNAME.json` – all collected info
- `--output pretty` – shows clean summary in terminal

---

## Required API Keys

Insert your API keys into these files:
- `email_scan.py` → `YOUR_HIBP_API_KEY`
- `phone_scan.py` → `YOUR_NUMVERIFY_API_KEY`

---

## Legal Disclaimer

This tool is intended **only for authorized use**. Do not scan or investigate individuals without explicit permission. Respect privacy laws and platform terms.

---

## Coming Soon

- PDF/HTML reporting
- Screenshot mode with Playwright
- Automatic relative discovery from public address records
