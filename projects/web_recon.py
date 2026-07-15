import requests
from bs4 import BeautifulSoup
import re
import json
from datetime import datetime
import pyinputplus as co


def web_recon():

    # ---------------------------
    # Get and validate URL
    # ---------------------------
    url = co.inputStr("Enter the target URL: ")

    if not re.fullmatch(r"https?://.+", url):
        print("❌ Invalid URL! URL must start with http:// or https://")
        return

    # ---------------------------
    # Download page
    # ---------------------------
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print("❌ Error downloading page.")
        print(e)
        return

    # ---------------------------
    # Parse HTML
    # ---------------------------
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()

    # ---------------------------
    # Extract Emails
    # ---------------------------
    emails = re.findall(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        text
    )

    emails = list(dict.fromkeys(emails))

    # ---------------------------
    # Extract IP Addresses
    # ---------------------------
    ips = re.findall(
        r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        text
    )

    ips = list(dict.fromkeys(ips))

    # ---------------------------
    # Extract Links
    # ---------------------------
    external_links = []
    internal_links = []

    for link in soup.find_all("a"):

        href = link.get("href")

        if href:

            if href.startswith("http"):
                external_links.append(href)

            elif href.startswith("/"):
                internal_links.append(href)

    external_links = list(dict.fromkeys(external_links))
    internal_links = list(dict.fromkeys(internal_links))

    # ---------------------------
    # Display Results
    # ---------------------------
    print("\n==============================")
    print("📧 Emails Found")
    print("==============================")

    if emails:
        for email in emails:
            print("→", email)
    else:
        print("No emails found.")

    print("\n==============================")
    print("🌐 IP Addresses Found")
    print("==============================")

    if ips:
        for ip in ips:
            print("→", ip)
    else:
        print("No IP addresses found.")

    print("\n==============================")
    print("🔗 External Links")
    print("==============================")

    if external_links:
        for link in external_links:
            print("→", link)
    else:
        print("No external links found.")

    print("\n==============================")
    print("🏠 Internal Links")
    print("==============================")

    if internal_links:
        for link in internal_links:
            print("→", link)
    else:
        print("No internal links found.")

    # ---------------------------
    # Ask what to save
    # ---------------------------
    choice = co.inputMenu(
        [
            "emails",
            "ips",
            "external_links",
            "internal_links",
            "everything"
            
        ],
        prompt="\nWhat would you like to save?\n"
    )

    results = {
        "emails": emails,
        "ips": ips,
        "external_links": external_links,
        "internal_links": internal_links,
        "everything" : {
            "emails": emails,
            "ips": ips,
            "external_links": external_links,
            "internal_links": internal_links,}
    }

    report = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "target": url,
        "category_saved": choice,
        "data": results[choice]
    }

    with open("recon_report.json", "w") as file:
        json.dump(report, file, indent=4)

    print("\n✅ Report saved as recon_report.json")


web_recon()