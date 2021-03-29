# buildItWebcrawler


# Overview


Web crawler project written in Python

The crawler should be limited to one domain. Given a starting URL – say http://wiprodigital.com - it should visit all pages within the domain, but not follow the links to external sites such as Google or Twitter.

The output should be a simple structured site map (this does not need to be a traditional XML sitemap - just some sort of output to reflect what your crawler has discovered) showing links to other pages under the same domain, links to external URLs, and links to static content such as images for each respective page.

Please provide a README.md file that explains how to build, test, and run your solution. Also, detail anything further that you would like to achieve with more time.

Please make your solution available on Github and forward the link. Where possible please include your commit history to provide visibility of your thinking and working practice.
What you need to share with us

A working crawler as per requirements above

A README.md explaining

How to build and run your solution (including any required installations)

Reasoning and describe any trade offs

Explanation of what could be done with more time

Project builds / runs / tests as per instruction

# Reasoning and Explain any trade offs


# TODO


1. I check to confirm that the http://www.wiprodigital.com’s owners allow scraping by  reading the Terms & Conditions and the Privacy Policy of the website.
2. Can I scrape the parts you are interested in? I checked the robots.txt file for more information and uses a tool that can handle this information.
3. What technology does the website use? 
>>> from builtwith import builtwith
>>> 
>>> builtwith('http://www.wiprodigital.com')
>>> 
>>> {'tag-managers': ['Google Tag Manager'], 'marketing-automation': ['Marketo', 'Yoast SEO'], 'javascript-frameworks': ['Modernizr', 'Prototype', 'jQuery'], 'web-frameworks': ['Twitter Bootstrap'], 'cms': ['WordPress'], 'programming-languages': ['PHP'], 'blogs': ['PHP', 'WordPress']}




