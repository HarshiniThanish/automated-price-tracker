from scraper.database import create_database
from scraper.scraper import scrape_products


def main():
    print("Starting price tracker...")
    create_database()

    try:
        count = scrape_products()
        print(f"Scraping completed successfully. {count} products collected.")
    except Exception as error:
        print(f"Scraping failed: {error}")


if __name__ == "__main__":
    main()
