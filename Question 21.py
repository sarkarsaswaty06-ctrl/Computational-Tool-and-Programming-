
import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Demo e-commerce website
url = "https://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

products = []

while url:
    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all product containers
    books = soup.select("article.product_pod")

    for book in books:
        title_tag = book.select_one("h3 a")
        price_tag = book.select_one(".price_color")
        stock_tag = book.select_one(".availability")
        rating_tag = book.select_one("p.star-rating")

        title = (
            title_tag.get("title", title_tag.get_text(strip=True))
            if title_tag else "N/A"
        )

        product_link = (
            urljoin(url, title_tag["href"])
            if title_tag and title_tag.get("href")
            else "N/A"
        )

        price = (
            price_tag.get_text(strip=True)
            if price_tag else "N/A"
        )

        availability = (
            stock_tag.get_text(" ", strip=True)
            if stock_tag else "N/A"
        )

        rating = (
            rating_tag.get("class", ["N/A"])[1]
            if rating_tag and len(rating_tag.get("class", [])) > 1
            else "N/A"
        )

        products.append({
            "Product Name": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Product URL": product_link
        })

    # Move to the next page, if available
    next_link = soup.select_one("li.next a")

    if next_link:
        url = urljoin(url, next_link["href"])
    else:
        url = None

# Save scraped data to CSV
filename = "products.csv"

with open(filename, "w", newline="", encoding="utf-8") as file:
    fieldnames = [
        "Product Name",
        "Price",
        "Rating",
        "Availability",
        "Product URL"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)

print("Product scraping completed successfully!")
print("Total products scraped:", len(products))
print("Data saved to", filename)
