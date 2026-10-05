# Dream2000 Web Scraping Project

## Project Description

This project is a web scraping application developed in Python to collect product information from the Dream2000 online store.

The scraper automatically visits all available pages in the product collection, extracts product information from the HTML source code, removes duplicate products, and stores the final dataset in a CSV file.

## Website

Dream2000:

https://dream2000.com/

Products collection:

https://dream2000.com/collections/all

## Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas
* JSON
* HTML
* CSV

## Scraping Process

The scraping program performs the following steps:

1. Connects to the Dream2000 products collection.
2. Identifies the total number of available pages.
3. Visits every page automatically.
4. Retrieves the complete HTML source code of each page.
5. Parses the HTML using BeautifulSoup.
6. Extracts product information from the HTML.
7. Stores the extracted products.
8. Removes duplicate products using the product ID.
9. Saves the final dataset into a CSV file.
10. Saves the complete terminal output into a separate text file named `terminal_output.txt`.

## Extracted Product Information

The following information is collected for each product:

* Page number
* Product ID
* Product name
* Current price
* Old price
* Availability
* Quantity
* Price with currency
* Product URL

## Final Results

The final scraping process successfully processed:

* **Total pages scraped:** 239
* **Total unique products:** 5515
* **Output CSV file:** `dream2000_products.csv`

The final dataset contains **5515 unique products** collected from all 239 pages.

## Project Files

```text
Dream2000-/
│
├── scraping.py
├── dream2000_products.csv
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

* **`scraping.py`** — The main Python web scraping program.
* **`dream2000_products.csv`** — The final dataset containing 5515 unique products.
* **`requirements.txt`** — Contains the Python libraries required to run the project.
* **`README.md`** — Contains the project documentation.
* **`.gitignore`** — Prevents large or unnecessary files from being uploaded to GitHub.

### Local Output File

When the scraper is executed, it also creates:

```text
terminal_output.txt
```

This file contains the complete terminal output, including the HTML source code retrieved during the scraping process. Because this file can be very large, it is excluded from the GitHub repository using `.gitignore`.

## Installation

Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

## How to Run

Run the scraping program using:

```bash
python scraping.py
```

The program will automatically:

* Detect the total number of pages.
* Visit all available pages.
* Retrieve the HTML source code.
* Extract product information.
* Remove duplicate products.
* Save the results to `dream2000_products.csv`.
* Save the terminal output to `terminal_output.txt`.

## Conclusion

The Dream2000 web scraping project successfully collected product information from all available product pages.

A total of **239 pages** were scraped, resulting in **5515 unique products**.

The collected product data is stored in the structured CSV file `dream2000_products.csv`, while the complete terminal output is saved locally in `terminal_output.txt`.
