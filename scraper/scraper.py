import requests
from bs4 import BeautifulSoup

from scraper.database import save_product

BASE_URL = "https://books.toscrape.com/"


def scrape_products():
    response = requests.get(
        BASE_URL,
        timeout=15,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.select("article.product_pod")

    scraped_count = 0

    for product in products:
        name = product.select_one("h3 a")["title"]
        price_text = product.select_one(".price_color").text.strip()
        price = float(price_text.replace("£", ""))

        relative_url = product.select_one("h3 a")["href"]
        product_url = BASE_URL + relative_url.replace("../../", "")

        save_product(
            product_name=name,
            price=price,
            currency="GBP",
            product_url=product_url
        )

        scraped_count += 1

    return scraped_count
