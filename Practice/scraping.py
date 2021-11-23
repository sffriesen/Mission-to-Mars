#!/usr/bin/env python
# coding: utf-8

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Set up executable path
executable_path = {"executable_path": ChromeDriverManager().install()}
browser = Browser("chrome", **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("div.list_text", wait_time=1)

# Set up the html parser
html = browser.html
news_soup = soup(html, "html.parser")
slide_elem = news_soup.select_one("div.list_text")

# Scrape the title into a parent element
slide_elem.find("div", class_="content_title")

# Use the parent element to find the first 'a' tag and save is as 'news_title'
news_title = slide_elem.find("div", class_="content_title").get_text()
news_title

# Scrape the summary into a parent element
slide_elem.find("div", class_="article_teaser_body")

# Use the parent element to find the paragraph text
news_p = slide_elem.find("div", class_="article_teaser_body").get_text()
news_p


# ### Featured Images

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and clock the full image button
full_image_elem = browser.find_by_tag("button")[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find("img", class_="fancybox-image").get("src")
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# Pull the first table from the Mars Facts page and turn it into a pd dataframe
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns = ["description", "Mars", "Earth"]
df.set_index("description", inplace=True)
df

# Turn the df into HTML
df.to_html()

# Quit automated browsing session
browser.quit()