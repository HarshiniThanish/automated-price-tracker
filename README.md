# Automated Web Scraper & Price Tracker

A Python-based automated price tracking pipeline that collects product pricing data from a public demo e-commerce website, stores historical records in SQLite, and runs automatically using GitHub Actions.

The collected data can be connected to Power BI to analyze historical price movements and pricing trends.

## Features

- Automated web scraping using Python
- HTML parsing with BeautifulSoup
- Structured price storage using SQLite
- Historical price tracking
- Scheduled execution using GitHub Actions
- Automated testing using pytest
- Power BI-ready database structure
- Basic error handling and request timeout
- Modular project architecture

## Architecture

```text
E-commerce Website
        |
        v
Python Scraper
Requests + BeautifulSoup
        |
        v
SQL Database (SQLite)
        |
        v
Power BI Dashboard

GitHub Actions
      |
      v
Scheduled Execution
```

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Scraper and automation |
| Requests | HTTP requests |
| BeautifulSoup | HTML parsing |
| SQLite | Data storage |
| Pytest | Automated testing |
| GitHub Actions | Scheduled execution |
| Power BI | Data visualization |
| Git | Version control |

## Project Structure

```text
automated-price-tracker/
|
├── scraper/
│   ├── __init__.py
│   ├── scraper.py
│   └── database.py
|
├── data/
│   └── .gitkeep
|
├── tests/
│   └── test_database.py
|
├── .github/
│   └── workflows/
│       └── daily_scraper.yml
|
├── .gitignore
├── requirements.txt
├── config.py
├── main.py
└── README.md
```

## Installation

### Clone

```bash
git clone https://github.com/YOUR_USERNAME/automated-price-tracker.git
cd automated-price-tracker
```

### Create virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Scraper

```bash
python main.py
```

Expected output:

```text
Starting price tracker...
Scraping completed successfully. 20 products collected.
```

The SQLite database is created at:

```text
data/price_tracker.db
```

## Database Schema

| Column | Description |
|---|---|
| id | Unique record identifier |
| product_name | Product name |
| price | Product price |
| currency | Price currency |
| product_url | Product page URL |
| scraped_at | Collection timestamp |

## GitHub Actions

The workflow runs once per day and can also be triggered manually.

```text
Checkout
   |
Setup Python
   |
Install dependencies
   |
Run tests
   |
Run scraper
```

> Note: GitHub-hosted runners are ephemeral. For persistent production data, use a hosted PostgreSQL database instead of storing SQLite only inside the runner.

## Power BI

The database can be used to build dashboards showing:

- Price history
- Current price
- Minimum and maximum recorded price
- Average price
- Product-level trends
- Price changes over time

## Testing

```bash
pytest
```

## Future Improvements

- PostgreSQL integration
- Selenium support for JavaScript-rendered websites
- Price-drop detection
- Email or Telegram alerts
- REST API
- Docker deployment
- Advanced Power BI dashboards
- Retry logic
- Structured logging
- Duplicate handling

## Ethical Scraping

This project is intended for educational and portfolio purposes.

When adapting it to another website:

- Respect the website's terms of service.
- Check robots.txt where applicable.
- Avoid excessive request rates.
- Do not bypass authentication, CAPTCHAs, or access controls.
- Prefer official APIs when available.
- Only collect data you are permitted to access.

## License

MIT License
