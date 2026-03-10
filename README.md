# quotes-web-scraper
Web Scraping project using Python and BeautifulSoup
# Quotes Web Scraper

## Project Overview

This project is a **web scraping application built with Python** that extracts quotes from the website http://quotes.toscrape.com.
The scraper collects quotes from the website pages and filters quotes that contain the **"life" tag**.

The extracted data includes the **quote text and author name**.

---

## Tools & Technologies Used

* Python
* Requests
* BeautifulSoup
* lxml
* Jupyter Notebook

---

## Project Workflow

1. Send HTTP requests to the website.
2. Download HTML pages containing quotes.
3. Parse the HTML using BeautifulSoup.
4. Extract quotes that contain the **life** tag.
5. Display the extracted quotes.

---

## Project Structure

quotes-web-scraper

scraping_activity.ipynb → Jupyter notebook containing the scraping code
scraper.py → Python script for scraping quotes
requirements.txt → Python libraries required to run the project
README.md → Project documentation
scraped_data/ → Folder containing downloaded HTML pages

---

## Installation

Clone the repository:

git clone https://github.com/yourusername/quotes-web-scraper.git

Navigate to the project folder:

cd quotes-web-scraper

Install required libraries:

pip install -r requirements.txt

---

## Running the Project

Run the scraper using:

python scraper.py

The script will scrape the website pages and extract quotes containing the **life** tag.

---

## Learning Outcome

Through this project I learned:

* Basics of **web scraping**
* Parsing HTML using **BeautifulSoup**
* Extracting data using **CSS selectors**
* Automating data collection using Python
* Organizing a project for **GitHub**

---

## Future Improvements

* Scrape quotes from **all pages automatically**
* Save extracted quotes into a **CSV dataset**
* Build a **data analysis project using the scraped dataset**
* Add **automation using Selenium for dynamic websites**

---

## Author

GitHub: https://github.com/gurleen55555
