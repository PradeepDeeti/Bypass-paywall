from bs4 import BeautifulSoup
import requests
import re

url = input("Enter the URL: ")

response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, 'html.parser')

text = soup.prettify()

pattern = r"<p [\s\S]{1,1000}</p>"

matches = re.findall(pattern, text)

output = " ".join(map(str, matches))

matches2 = re.sub(r"<[\s\S]+?>", " ", output)
output2 = re.sub(r"\n\n\n", "\n", matches2)
finaloutput = re.sub(r"\n\s{1,20}\n", "\n", output2)

print(output2)
