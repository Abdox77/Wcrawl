from scrapers.base_scraper import BaseScraper

class DDscraper(BaseScraper):
    """
    """

    def process_page(self, url, soup):
        data = super().process_page(url, soup)
        data["h1_tags"] = [h1.text.strip() for h1 in soup.find_all('h1')]
        data["p_count"] = len(soup.find_all('p'))
        return data

if __name__ == "__main__":
    url = "https://scrapeMe.com"
    scraper = DDscraper(
        start_url = url,
        max_pages = 5,
        delay = 10.0,
        same_domain_only=True 
    )

    results = scraper.crawl()
    scraper.save_data("scrapeMe_crawl.txt")
    print(f'Crawled {len(results)} pages')
