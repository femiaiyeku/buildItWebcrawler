from urllib.request import urlopen
from urllib.parse import urljoin
import re

""" Extract image location link """

def download_page(url) -> object:
    return urlopen(url).read().decode('utf-8')


def extract_img_locations(page):
    img_regex = re.compile('<img[^>]+src=["\'](.*?)["\']', re.IGNORECASE)
    return img_regex.findall(page)


if __name__ == '__main__':
    target_url = 'http://www.wiprodigital.com'
    wipro_digital_img = download_page(target_url)
    img_locations = extract_img_locations(wipro_digital_img)

    for src in img_locations:
        print(urljoin(target_url, src))
