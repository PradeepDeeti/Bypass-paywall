import requests
from bs4 import BeautifulSoup
import re

# URL to scrape
inputurl = input("enter the url: ")

url = "https://archive.ph/"+inputurl


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Getting the webpage, creating a Response object with fake User-Agent.
response = requests.get(url, headers=headers)
data=response.text

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all 'a' tags and extract the 'href' attribute

pattern= "https://archive.ph/[A-z0-9A-Z]{1,10}\""
matches=re.search(pattern, data)


print(matches)

