# Hikes_scraper Project

We're using Python's Scrapy, Selenium, Requests, BeautifulSoup, regex, and lambda functions to extract and manipulate hiking route details from [Komoot's Poland](https://www.komoot.com/discover/Poland/@52.2159330,19.1344220/tours?sport=hike&map=true&regionId=2486&max_distance=4.82) page.


## Project Introduction

Our project focuses on gathering information about hiking routes from Komoot, a leading platform for outdoor enthusiasts. We used a combination of web scraping tools and libraries in Python, including Scrapy for management and automation, Selenium for interaction and navigation, and BeautifulSoup for parsing and collecting data from JavaScript-enabled pages.

To ensure efficient extraction and processing of data, we used Scrapy spiders to automate website navigation, while Selenium facilitated interaction with dynamic content. Subsequently, we used BeautifulSoup to extract relevant information from the JavaScript-rendered pages. Additionally, we applied Python's regex and lambda functions to extract specific details from the collected dataset.

In summary, our project demonstrates our adeptness in gathering and analyzing hiking route information from online platforms, showcasing proficiency in web scraping techniques and data manipulation using Python.

## Project structure

The project structure consists of the following components:

```bash
.
├── README.md 
├── main.py
├── scrapy.cfg
└── web_scrapper
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── Project Description.ipynb
    ├── pipelines.py
    ├── settings.py
    └── spiders
        ├── __init__.py
        └── hiking_selenium.py
```
### Description detail:
We can see in the Project Description.ipynb file
