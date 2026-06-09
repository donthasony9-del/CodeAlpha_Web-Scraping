# CodeAlpha Web Scraping Project

## Project Name
Book Data Scraper using Python

---

# Project Overview

This project is developed for the CodeAlpha Data Analytics Internship.

The main purpose of this project is to collect book data automatically from a website using Python Web Scraping techniques.

The scraper extracts:
- Book Titles
- Book Prices
- Book Ratings
- Availability Status
- Product Links

The collected data is stored into:
- CSV File
- Excel File

---

# Website Used

Books To Scrape

```text
https://books.toscrape.com/
```

This website is specially designed for practicing web scraping projects.

---

# Main Concept

The project automatically:
1. Connects to the website
2. Reads HTML source code
3. Extracts required data
4. Cleans the data
5. Stores the data into files

This process is called:

# Web Scraping

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Requests | Sending HTTP Requests |
| BeautifulSoup4 | HTML Parsing |
| Pandas | Data Processing |
| OpenPyXL | Excel File Export |
| LXML | Fast HTML Parser |

---

# Python Libraries Used

```text
requests
beautifulsoup4
pandas
lxml
openpyxl
```

---

# Project Structure

```text
CodeAlpha-WebScraping-Project/
│
├── scraper.py
├── books_data.csv
├── books_data.xlsx
├── requirements.txt
├── README.md
├── screenshots
└── outputs/
```books_data.csx
   books_data.xlsx
---

# Features

✅ Multi-page scraping  
✅ Automatic data collection  
✅ CSV export  
✅ Excel export  
✅ Logging system  
✅ Error handling  
✅ Data cleaning  
✅ Professional folder structure  

---

# Data Extracted

The scraper collects:

| Field Name | Description |
|---|---|
| Title | Name of the Book |
| Price | Book Price |
| Availability | Stock Status |
| Rating | Star Rating |
| Product Link | Book URL |
| Scraped Time | Date and Time |

---

# How The Project Works

```text
Website
   ↓
Send Request
   ↓
Download HTML
   ↓
Parse HTML using BeautifulSoup
   ↓
Extract Data
   ↓
Store Data using Pandas
   ↓
Export CSV and Excel Files
```

---

# Installation

Install required libraries using:

```bash
python -m pip install -r requirements.txt
```

---

# Run The Project

Execute the scraper:

```bash
python scraper.py
```

---

# Terminal Output

```text
==================================================
CODEALPHA WEB SCRAPING PROJECT
==================================================
Total Books Scraped : 100
CSV File            : books_data.csv
Excel File          : books_data.xlsx
PROJECT STATUS      : SUCCESS
==================================================
```

---

# Output Files

After running the project:

✅ books_data.csv  
✅ books_data.xlsx  

will be generated automatically.

---

# Sample Output Data

| Title | Price | Rating |
|---|---|---|
| A Light in the Attic | 51.77 | Three |
| Tipping the Velvet | 53.74 | One |

---

# Data Cleaning Performed

The project performs:
- Duplicate removal
- Null value removal
- Price cleaning
- Structured data formatting

---

# Screenshots

Add screenshots inside:

```text
screenshots/
```

Recommended screenshots:
- VS Code Project
- Terminal Output
- CSV Output
- Excel Output

---

# Why This Project Is Useful

This project helps in:
- Learning Web Scraping
- Data Collection Automation
- Data Analytics Workflow
- Python Automation
- Real-world Data Handling

---

# Future Improvements

⭐ Streamlit Dashboard  
⭐ Data Visualization  
⭐ Database Integration  
⭐ Sentiment Analysis  
⭐ Real-time Scraping   
---

# Internship Task

CodeAlpha Data Analytics Internship

Task 1 — Web Scraping

---

# Author

SRINITHA K

---

# License

This project is created for educational and internship purposes only.