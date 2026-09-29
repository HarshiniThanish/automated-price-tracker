from scraper.database import DATABASE_PATH, create_database


def test_database_creation():
    create_database()
    assert DATABASE_PATH.exists()
