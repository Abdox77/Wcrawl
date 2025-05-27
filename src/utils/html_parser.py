from bs4 import BeautifulSoup
import requests
from typing import Optional, Dict, Any


def get_soup(url: str, headers: Optional[Dict[str, str]] = None) -> BeautifulSoup:
    """
    Fetch a web page and return a BeatifulSoup object

    Args:
        url: The URL to fetch
        headers: Optional HTTP headers

    Returns:
        BeautifulSoup object
    """

    default_headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    if headers: 
        default_headers.update(headers)
    response = requests.get(url, headers=default_headers)
    response.raise_for_status() 
    return BeautifulSoup(response.text, 'lxml')


def extract_links(soup: BeautifulSoup, base_url: str = "") -> list[str]:
    """
    Extract all linkis from a BeautifulSoup object

    Args:
        soup: BeatifulSoup object
        base_url: Base URL to prepend to relative links
    
    Returns:
        List of URLs
    """

    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startwith('http'):
            links.append(href)
        elif base_url and href.startswith('/'):
            links.append(f"{base_url.rstrip('/')}{href}")
    
    return links
