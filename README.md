# Wcrawl

A simple Python web crawler for extracting data from websites.

## Overview

Wcrawl is a lightweight web scraping framework built with BeautifulSoup and requests. It provides a base crawler class that can be extended to extract custom data from web pages.

## Features

- Configurable crawling depth and delay
- Same-domain filtering
- Extensible page processing
- Data export to text files

## Usage

```python
from scrapers.base_scraper import BaseScraper

class CustomScraper(BaseScraper):
    def process_page(self, url, soup):
        data = super().process_page(url, soup)
        # Add custom extraction logic
        return data

scraper = CustomScraper(
    start_url="https://example.com",
    max_pages=10,
    delay=1.0,
    same_domain_only=True
)

results = scraper.crawl()
scraper.save_data("output.txt")
```

## Installation

```bash
pip install beautifulsoup4 requests lxml
```

## Running

```bash
make run
```

## Structure

- `scrapers/` - Crawler implementations
- `utils/` - HTML parsing utilities
- `main.py` - Example usage

## Requirements

- Python 3.7+
- BeautifulSoup4
- requests
- lxml