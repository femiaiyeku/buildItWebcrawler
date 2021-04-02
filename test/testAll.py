import unittest
from src.url_name import get_url_name
from src.robot_txt import is_allowed
from src.extract_link import extract_links
from src.img_location import extract_img_locations


class TestMain(unittest.TestCase):
    def test_get_url_name(self):
        result = get_url_name(url='http://www.wiprodigital.com')
        self.assertEqual(result, "")

    def test_is_allowed(self):
        robot_txt = is_allowed(user_agent='*', target_url='http://www.wiprodigital.com')
        self.assertEqual(robot_txt, "")

    def test_extract_img_locations(self):
        image_loc = extract_img_locations(page='http://www.wiprodigital.com')
        self.assertEqual(image_loc, "")

    def test_extract_links(self):
        link = extract_links(page='http://www.wiprodigital.com')
        self.assertEqual(link, "")

        if __name__ == '__main__':
            unittest.main()
