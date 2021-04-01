from urllib import robotparser

""""Parse the robots.txt file of the target website and acts based on the contents"""

robot_parser = robotparser.RobotFileParser()


def prepare(robots_txt_url):
    robot_parser.set_url(robots_txt_url)
    robot_parser.read()


def is_allowed(target_url, user_agent='*'):
    return robot_parser.can_fetch(user_agent, target_url)


if __name__ == '__main__':
    prepare('http://wiprodigital.com/robots.txt')

    print(is_allowed('http://wiprodigital.com/wp-admin/', 'wp-admin'))
    print(is_allowed('https://wiprodigital.com/wp-admin/admin-ajax.php', 'admin-ajax.php'))
