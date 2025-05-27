import os
import time
from typing import List, Set, Dict, Any, Optional
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from utils.html_parser import get_soup, extract_links


class BaseScraper:
    def __init__(self, 
                start_url: str,
                max_pages: int = 10,
                delay: float = 1.0,
                same_domain_only: bool = True,
                output_dir: str = "../data/output") :
        """
        Initialze the base scraper

        Args:
            start_url: The starting URL for the crawler
            max_pages: Maximum number of pages to crawl
            delay: Delay between requests in seconds
            same_domain_only: Only follow links within the same domain
            output_dir: Directory to save output files
        """

        self.start_url = start_url
        self.max_pages = max_pages
        self.delay = delay
        self.same_domain_only = same_domain_only
        self.output_dir = output_dir

        parsed_url = urlparse(start_url)
        self.domain = parsed_url.netloc

        self.visited_urls: Set[str] = set()
        self.urls_to_visit: List[str] = [start_url]
        self.data: List[Dict[str, Any]] = []

    def crawl(self) -> List[Dict[str,Any]]:
        """
        Starts the crawling process

        Returns:
            List of extracted data
        """
        count = 0

        while self.urls_to_visit and count < self.max_pages:
            url = self.urls_to_visit.pop(0)
            if url in self.visited_urls:
                continue
            print(f'Crawling: {url}')
            
            try:
                soup = get_soup(url)
                page_data = self.process_page(url, soup)
                if page_data:
                    self.data.append(page_data)

                links = extract_links(soup, self.start_url)

                if self.name_domain_only:
                    links = [links for link in links if urlparse(link).netloc == self.domain]
                
                for link in links:
                    if link not in self.visited_urls and link not in self.urls_to_visit:
                        self.urls_to_visit.append(link)
                
                self.visited_urls.add(url)
                count += 1
                time.sleep(self.delay)
            except Exception as err:
                print(f'Error crawling {url}: {e}')
        
        return self.data


def save_data(self, filename: str= "crawled_data.txt") -> None:
    """
    Save the crawled data to a file

    Args:
        filename: Name of the file to save data
    """
    os.makedirs(self.output_dir, exist_ok=True)
    output_path = os.path.join(self.output_dir, filename)
    with open(output_path, 'w', encoding='utf-8') as f:
        for item in self.data:
            f.write(f"{str(item)}\n")
    print(f"Data saved to {output_path}")
