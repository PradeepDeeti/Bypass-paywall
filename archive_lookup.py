import requests
import re
import sys

if len(sys.argv) == 2:
    inputurl = sys.argv[1]
else:
    inputurl = input("Enter the URL: ").strip()


url = "https://archive.ph/" + inputurl

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)
data = response.text

# \" is important element in the regex to avoid false positives hence keeping it in regex and trimming it later
pattern = r"https://archive.ph/[A-Za-z0-9]{1,10}\""
matches = re.search(pattern, data)

if matches:
    ur = matches.group()
    cleaned_url = ur.rstrip('"')
    print("\n archive for "+ inputurl+" = "+cleaned_url+"\n")
else:
    print("No matches found.")
