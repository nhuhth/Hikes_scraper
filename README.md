# Hikes_scraper Project

## <div align="center"> Scraping Komoot Website for Customized Hike Suggestions</div>

This project utilizes Python's Scrapy, Selenium, Requests, BeautifulSoup, regex, and lambda functions to extract and manipulate hiking route details from [Komoot's Poland](https://www.komoot.com/discover/Poland/@52.2159330,19.1344220/tours?sport=hike&map=true&regionId=2486&max_distance=4.82) page.

## Project Introduction

Our project focuses on gathering information about hiking routes from Komoot, a leading platform for outdoor enthusiasts. We employed a combination of web scraping tools and libraries in Python, including:

- **Scrapy** for management and automation of the scraping process.
- **Selenium** for interacting with dynamic web content.
- **BeautifulSoup** for parsing and extracting data from JavaScript-enabled pages.
- **Requests** for handling HTTP requests efficiently.
- **Regex and lambda functions** for refining and processing extracted data.

To ensure efficient extraction and processing, Scrapy Spiders were used to automate website navigation, while Selenium facilitated interaction with dynamic content. BeautifulSoup was then employed to parse and extract relevant information from JavaScript-rendered pages. 

### Key Features
- Automated scraping of hiking routes.
- Interaction with JavaScript-rendered content.
- Data extraction, cleaning, and formatting using Python.
- Structured dataset creation for further analysis.

### Project Files
- **Project Description.ipynb**: Detailed explanation of project workflow and implementation.
- **scrapy_spiders/**: Contains Scrapy spider scripts for automating the scraping process.
- **data/**: Folder containing extracted hiking route data.
- **requirements.txt**: List of dependencies required for running the project.

## Installation & Usage

### Prerequisites
- Python 3.x
- Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Scraper
```bash
scrapy crawl hikes_spider
```

## Future Improvements
- Expanding to other regions on Komoot.
- Implementing NLP for enhanced route recommendations.
- Improving data storage and visualization.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
