"""
🔗 Web Scraping Demo: Following Links with BeautifulSoup

📌 Description:
This Python script demonstrates web scraping using the `urllib` and `BeautifulSoup` libraries.
The program:
1. Reads a starting URL from the user.
2. Finds all the `<a>` (anchor) tags on the page.
3. Iteratively follows links based on user-defined **position** and **count**.
4. Prints each retrieved URL in the chain.

✅ Skills Demonstrated:
- Web scraping with BeautifulSoup
- Handling SSL certificate errors
- Iterative link navigation
- String & list manipulation
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# -------------------- Step 1: Handle SSL certificate errors --------------------
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# -------------------- Step 2: User inputs --------------------
url = input('Enter starting URL: ')   # Example: http://py4e-data.dr-chuck.net/known_by_Fikret.html
count = int(input('Enter count: '))   # How many times to follow the link
position = int(input('Enter position: ')) - 1  # Which link to follow each time

# -------------------- Step 3: Follow links iteratively --------------------
print("\n--- Starting Web Scraping Demo ---")
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Extract all anchor tags
    tags = soup('a')
    url = tags[position].get('href')

    print(f"Step {i+1}: Retrieving {url}")

print("\n--- Demo Completed ---")
