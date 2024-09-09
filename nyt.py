from bs4 import BeautifulSoup
import requests
import re

# Get URL from user input
url = input("Enter the URL: ")

# Define a fake User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Getting the webpage, creating a Response object with fake User-Agent.
response = requests.get(url, headers=headers)

# Extracting the source code of the page.
data = response.text

# Passing the source code to Beautiful Soup to create a BeautifulSoup object for it.
soup = BeautifulSoup(data, 'html.parser')

text = soup.prettify()

pattern = r"<p [\s\S]{1,1000}</p>"

matches = re.findall(pattern, text)

# Join matches into a single string separated by commas
output = " ".join(map(str, matches))

# Remove HTML tags and excessive newlines
matches2 = re.sub(r"<[\s\S]+?>", " ", output)
output2 = re.sub(r"\n\n\n", "\n", matches2)
new2 = re.sub(r"\n\s{1,20}\n", "\n", output2)
another = re.sub(r"\n\s{1,20},", "\n", new2)
al = re.sub(r"^\s{3,20}", "\n", another)

print(al)
