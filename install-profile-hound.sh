#!/bin/bash

echo "[*] Installing profile-hound dependencies..."

# Ensure Python3 and pip are installed
if ! command -v python3 &>/dev/null; then
    echo "[!] Python3 is not installed. Aborting."
    exit 1
fi

if ! command -v pip3 &>/dev/null; then
    echo "[!] pip3 is not installed. Installing it..."
    sudo apt update && sudo apt install -y python3-pip
fi

# Install base requirements
pip3 install --user -r requirements.txt

# Ask if user wants full headless browser support
read -p "[?] Install headless browser support (Selenium + Playwright)? [y/N]: " browser_support
if [[ "$browser_support" =~ ^[Yy]$ ]]; then
    echo "[*] Installing full browser automation stack..."
    pip3 install --user -r requirements-full.txt
    echo "[*] Installing Playwright browsers..."
    python3 -m playwright install
fi

# Create results directory
mkdir -p results

echo "[+] profile-hound is installed. Run it with: python3 profile_hound.py --help"
