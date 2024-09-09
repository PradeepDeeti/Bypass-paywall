Bypass the paywall by accessing a archived snapshot at archive.ph


This guide provides instructions for two Python scripts: archive_lookup.py and archive_pop.py. 

These scripts fetch archive URLs from archive.ph based on a provided URL, with archive_pop.py also opening the fetched URL in a new browser window using Selenium. Using either one as per your preference.

Dependencies:

requests, beautifulsoup, selenium (for achive_popup.py)

To install these dependencies, run:

pip install requests beautifulsoup4 selenium

Default Packages:

The scripts also use re (for regular expressions) and time (for pauses), which are part of Python's standard library, so no additional installation is required.

Installation:

Download the archive_lookup.py and archive_pop.py files.

Save them to your desired location.

Usage:

1. archive_lookup.py
-------------------------

This script fetches an archive URL from archive.ph based on a given URL.

Command-line Usage:

python archive_lookup.py https://example.com

example output: archive for https://example.com = https://archive.ph/PfOkY

---------------------------

2. archive_pop.py
---------------------------

This script fetches the archive URL from archive.ph and opens it in a new browser window using Selenium.

Command-line Usage:

python archive_pop.py https://example.com

----------------------------

Additional Requirements

For archive_pop.py, you need:

Google Chrome browser installed on your system.
ChromeDriver installed and set up. Update the path to chromedriver in the script as needed.
