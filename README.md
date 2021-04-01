# buildItWebcrawler


# Overview

Web crawler project written in Python

The crawler should be limited to one domain. Given a starting URL – say http://wiprodigital.com - it should visit all pages within the domain, but not follow the links to external sites such as Google or Twitter.

The output should be a simple structured site map (this does not need to be a traditional XML sitemap - just some sort of output to reflect what your crawler has discovered) showing links to other pages under the same domain, links to external URLs, and links to static content such as images for each respective page.

Please provide a README.md file that explains how to build, test, and run your solution. Also, detail anything further that you would like to achieve with more time.




# Requirement


1. I check to confirm that the http://www.wiprodigital.com’s owners allow scraping by  reading the Terms & Conditions and the Privacy Policy of the website.
2. Can I scrape the parts you are interested in? I checked the robots.txt file for more information and uses a tool that can handle this information.



# Install python packages

pip3 install -r requirements.txt

# Test case


# Execute the crawler file


python3 ./main.py


# TODO


• Configure git repository, Go crawl and scrape the webpage 

• Main.py is the main script which will run in terminal.

• Place all other supporting scripts in the src directory.

• Add Test to the test directory

• Scrapes all static assets held on the wiprodigital.com domain

• Update the README.md

• Run the main.py code


# Reasoning

•Create a monitoring process. 

•Data on the website might be timed

•Increase unit testing


# Tradeoff

• Web scraping run much faster and require much less bandwidth when they don’t have
to download files.

• You save space on your computer/cloud storage by storing only the URLs.

• It is easier to write code that stores only URLs and doesn’t need to deal with additional file downloads.

• One of the most difficult parts of gathering data through scraping websites is that websites differ. I mean not only the data but the layout too. It is hard to create a good-fit-for-all scraper because every website has a different layout.

• Websites change their layout frequently. If this happens, the scraper is not working as it did previously. In these case, the other option is to revisit your code and adapt it to the changes of the target website.

•Try creating a long-lasting loop that rechecks certain URLs and scrapes data at set intervals

• Ensure that your acquired data is always fresh.

• Integrate proxies into your web scraper. Using location specific request sources allows you to acquire data that might otherwise be inaccessible.



