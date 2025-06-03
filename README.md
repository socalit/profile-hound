# profile-hound

`profile-hound` is a modular Python-based CLI OSINT tool for investigating usernames, phone numbers, and email addresses across the internet. It can scan social media, check breach data, validate phone numbers, and (optionally) extract profile metadata using browser automation.

Built by [socalit](https://github.com/socalit) for ethical recon, cybersecurity auditing, and digital footprint analysis.

---

## 🔍 Features

- Username scanner across major platforms (Twitter, GitHub, Reddit, etc.)
- Email breach detection via HaveIBeenPwned API
- Phone metadata extraction using Numverify API
- Address/DOB/Relatives enrichment placeholder
- Optional: dynamic web scraping with Selenium or Playwright
- Multi-threaded
- Outputs to structured JSON

---

## Usage

```bash
# Basic username scan
python3 profile_hound.py --username johndoe

# Email breach check
python3 profile_hound.py --email user@example.com

# Phone lookup
python3 profile_hound.py --phone +15551234567

# Full profile (runs all checks)
python3 profile_hound.py --username johndoe --email user@example.com --phone +15551234567 --all
```

---

## Installation

```bash
# Clone the repo
git clone https://github.com/socalit/profile-hound.git
cd profile-hound

# Run the installer
chmod +x install-profile-hound.sh
./install-profile-hound.sh
```

During install, you'll be prompted to enable optional browser support (Selenium & Playwright).

---

## Output

- JSON results saved to `/results/target.json`
- Console summary if using `--output pretty`

---

## Project Structure

```
profile_hound.py               # CLI entry
modules/
  ├── username_scan.py         # Public profile checks
  ├── email_scan.py            # HIBP integration
  ├── phone_scan.py            # Numverify API
  └── address_enrichment.py    # Placeholder for PII lookups
results/                       # Output directory
```

---

## API Keys Required

To use full features, insert your keys into:

- `email_scan.py`: `YOUR_HIBP_API_KEY`
- `phone_scan.py`: `YOUR_NUMVERIFY_API_KEY`

---

## Legal & Ethical Notice

This tool is intended for **authorized use only**. Always ensure you have permission to investigate personal data. Use responsibly and ethically.

---

## Coming Soon

- PDF and HTML reports
- Browser-based viewer
- LinkedIn/Instagram/TikTok scraping via Playwright
# profile-hound
CLI OSINT tool for investigating usernames, phone numbers, and email addresses across the internet. It can scan social media, check breach data, validate phone numbers, and (optionally) extract profile metadata using browser automation.
