import time
import requests
from bs4 import BeautifulSoup
import re
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Get the URL from command-line arguments
inputurl = sys.argv[1] if len(sys.argv) > 1 else input("Enter the URL: ").strip()

url = "https://archive.ph/" + inputurl

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)
data = response.text

soup = BeautifulSoup(response.text, "html.parser")

# \" is important element in the regex to avoid false positives hence keeping it in regex and trimming it later
pattern = r"https://archive.ph/[A-Za-z0-9]{1,10}\""
matches = re.search(pattern, data)

if matches:
    ur = matches.group()
    cleaned_url = ur.rstrip('"')
    print("\nArchive for " + inputurl + " = " + cleaned_url + "\n")

    # Set up Selenium with ChromeDriver
    chrome_options = Options()
    chrome_options.add_argument("--new-window")  # Open in a new window
    chrome_options.add_argument("--start-maximized")  # Maximize the window

    # Specify the path to the chromedriver executable
    service = Service('Bypass-paywall/chromedriver-win64/chromedriver-win64/chromedriver.exe')

    driver = webdriver.Chrome(service=service, options=chrome_options)

    time.sleep(5)
    driver.get(cleaned_url)

    time.sleep(100)

else:
    print("No matches found.")
