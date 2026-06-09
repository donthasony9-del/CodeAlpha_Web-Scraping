import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
from datetime import datetime
import os

# ==========================================
# CODEALPHA WEB SCRAPING PROJECT
# ==========================================

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

TOTAL_PAGES = 5

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ==========================================
# GENERATE UNIQUE FILE NAMES
# ==========================================

def generate_filename(base_name, extension):

    counter = 1

    filename = f"{base_name}.{extension}"

    while os.path.exists(filename):

        counter += 1

        filename = f"{base_name}{counter}.{extension}"

    return filename

# ==========================================
# OUTPUT FILES
# ==========================================

CSV_FILE = generate_filename(
    "books_data",
    "csv"
)

EXCEL_FILE = generate_filename(
    "books_data",
    "xlsx"
)

# ==========================================
# SCRAPE SINGLE PAGE
# ==========================================

def scrape_page(page_number):

    url = BASE_URL.format(page_number)

    try:

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "lxml"
        )

        books = soup.find_all(
            "article",
            class_="product_pod"
        )

        page_data = []

        for book in books:

            title = book.h3.a["title"]

            price = book.find(
                "p",
                class_="price_color"
            ).text.strip()

            availability = book.find(
                "p",
                class_="instock availability"
            ).text.strip()

            rating = book.find(
                "p",
                class_="star-rating"
            )["class"][1]

            relative_link = book.h3.a["href"]

            product_link = (
                "https://books.toscrape.com/catalogue/"
                + relative_link
            )

            scraped_time = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            page_data.append({

                "Title": title,

                "Price": price.replace("£", ""),

                "Availability": availability,

                "Rating": rating,

                "Product Link": product_link,

                "Scraped Time": scraped_time

            })

        logging.info(
            f"Page {page_number} Scraped Successfully"
        )

        return page_data

    except Exception as error:

        logging.error(
            f"Error on Page {page_number}: {error}"
        )

        return []

# ==========================================
# MAIN FUNCTION
# ==========================================

def main():

    logging.info("Web Scraping Started")

    all_books = []

    for page in range(1, TOTAL_PAGES + 1):

        books = scrape_page(page)

        all_books.extend(books)

    # CREATE DATAFRAME
    df = pd.DataFrame(all_books)

    # CLEAN DATA
    df.drop_duplicates(inplace=True)

    df.dropna(inplace=True)

    # EXPORT CSV
    df.to_csv(
        CSV_FILE,
        index=False
    )

    logging.info(
        f"CSV File Saved: {CSV_FILE}"
    )

    # EXPORT EXCEL
    df.to_excel(
        EXCEL_FILE,
        index=False
    )

    logging.info(
        f"Excel File Saved: {EXCEL_FILE}"
    )

    # FINAL OUTPUT
    print("\n")

    print("=" * 50)

    print("CODEALPHA WEB SCRAPING PROJECT")

    print("=" * 50)

    print(f"Total Books Scraped : {len(df)}")

    print(f"CSV File            : {CSV_FILE}")

    print(f"Excel File          : {EXCEL_FILE}")

    print("PROJECT STATUS      : SUCCESS")

    print("=" * 50)

    print("\n")

# ==========================================
# DRIVER CODE
# ==========================================

if __name__ == "__main__":
    main()