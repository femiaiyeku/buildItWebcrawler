

from urllib.request import urlopen
from urllib.parse import urljoin
import re

"""Extracts all the links, which you can find at the Wipro Digital homepage"""

def download_page(url):
    return urlopen(url).read().decode('utf-8')


def extract_links(page):
    link_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return link_regex.findall(page)


if __name__ == '__main__':
    target_url = 'http://www.wiprodigital.com'
    wipro_digital = download_page(target_url)
    links = extract_links(wipro_digital)

    for link in links:
        print(urljoin(target_url, link))
