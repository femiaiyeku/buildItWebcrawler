import argparse
import requests
import logging
import http.client
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import re

URL = 'http://www.wiprodigital.com'


def parse_src():
    pass


def process_link(src_link):
    logging.info(f'Extracting links from {src_link}')
    urlparse(src_link)
    result = requests.get(src_link)
    if result.status_code != http.client.OK:
        logging.error(f'Error retrieving {src_link}: {result}')
        return src_link, []
    if 'html' not in result.headers['Content-type']:
        logging.info(f'Link {src_link} is not an HTML page')
        return []
    page = BeautifulSoup(result.text, 'html.parser')
    search_text(src_link, page, text)

    return get_links(page)


"""Retrieve the links on the page"""


def get_links(page):

    for element in page.find_all('a'):
        link = element.get('href')
        if not link:
            continue
            if link.startwith('#'):
                continue
                if link.startwith('mailto:'):  # Ignore other links like mailto
                    continue
                    if not link.startwith('http'):
                        netloc = parse_src.netloc
                        scheme = parse_src.scheme
                        path = urljoin(parse_src.path, link)
                        link = f'{scheme}://{netloc}{path}'
                        if parse.src.netloc not in link:
                            continue
                            links.append(link)
                            return links
                        """Search for an element with the search text and print it"""


def search_text(src_link, page, text):
    for element in page.find_all(re.compile(text, re.IGNORECASE)):
        print(f'Link {src_link}: --> {element}')


def main(base_url):
    checked_links = set()
    to_check = [base_url]
    max_checks = 10
    while to_check and max_checks:
        link = to_check.pop(0)
        links = process_link(link)
        checked_links.add(link)
        for link in links:
            if link not in checked_links:
                checked_links.add(link)
                to_check.append(link)
                max_checks -= 1
            if __name__ == '__main__':
                parser = argparse.ArgumentParser()
                parser.add_argument('url', type=str, help='Base-url' 'Use "http://www.wiprodigital.com"' 
                                                          'for scraping and crawling')
                parser.parse_args()
                if __name__ == '__main__':
                    main(args.url)
