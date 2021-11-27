# Mission-to-Mars

## Overview
This project was to use Python, MongoDB, and Flask to webscrape Mars information off of NASA's webpage, into a clean looking, mobile and desktop friendly, webpage.

I used BeautifulSoup and Splinter to scrape the needed information (the most recent Mars News article title and summary, a featured Mars image, a Mars Facts table, and images of Mars four hemispheres). This information was then stored in a MongoDB database.

The data was then displayed on a webpage using Flask. Bootstrap 3 components were used to make the webpage accessible both on desktop and mobile devices, and to customize certain aspects of the page, to make it look cleaner.

This webpage includes a "Scrape New Data" button, so that the most recent information can be displayed at any time.
