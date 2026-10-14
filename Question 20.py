

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Web page URL
url = "https://news.ycombinator.com/"

# Send HTTP request
response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=15
)
response.raise_for_status()

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser)

# Extract headlines and hyperlinks
headlines = soup.find_all("h2")

print("NEWS HEADLINES AND HYPERLINKS")
print("-" * 60)

count = 0

for headline in headlines:
    title = headline.get_text(" ", strip=True)
    link_tag = headline.find("a")

    if title and link_tag and link_tag.get("href"):
        link = urljoin(url, link_tag["href"])

        print("Headline:", title)
        print("Link:", link)
        print("-" * 60)

        count += 1

if count == 0:
    print("No headlines found. The website structure may have changed.")
