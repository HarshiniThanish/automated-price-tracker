import sqlite3
from pathlib import Path

DATABASE_PATH = Path("data/price_tracker.db")


def create_database():
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            price REAL NOT NULL,
            currency TEXT DEFAULT 'GBP',
            product_url TEXT NOT NULL,
            scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_product(product_name, price, currency, product_url):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO products
        (product_name, price, currency, product_url)
        VALUES (?, ?, ?, ?)
    """, (product_name, price, currency, product_url))

    connection.commit()
    connection.close()


def get_products():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT product_name, price, currency, product_url, scraped_at
        FROM products
        ORDER BY scraped_at DESC
    """)

    products = cursor.fetchall()
    connection.close()
    return products
