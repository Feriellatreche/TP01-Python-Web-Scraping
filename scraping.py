import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time
import sys

# ==============================
# 1. Save Terminal Output
# ==============================

terminal_file = open(
    "terminal_output.txt",
    "w",
    encoding="utf-8"
)

class Tee:
    def __init__(self, *files):
        self.files = files

    def write(self, text):
        for file in self.files:
            file.write(text)
            file.flush()

    def flush(self):
        for file in self.files:
            file.flush()

sys.stdout = Tee(sys.stdout, terminal_file)

# ==============================
# 2. Website
# ==============================

BASE_URL = "https://dream2000.com/collections/all"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/154.0.0.0 Safari/537.36"
    )
}

# ==============================
# 3. Get First Page
# ==============================

response = requests.get(
    BASE_URL,
    headers=headers,
    timeout=30
)

response.raise_for_status()

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

# ==============================
# 4. Find Total Number of Pages
# ==============================

pagination = soup.find(
    "nav",
    class_="pagination"
)

page_numbers = []

if pagination:
    for link in pagination.find_all(
        "a",
        href=True
    ):
        href = link["href"]

        if "page=" in href:
            try:
                page_number = int(
                    href.split("page=")[1]
                    .split("&")[0]
                )

                page_numbers.append(
                    page_number
                )

            except ValueError:
                pass

if page_numbers:
    total_pages = max(page_numbers)
else:
    total_pages = 1

print("=" * 70)
print(f"TOTAL NUMBER OF PAGES: {total_pages}")
print("=" * 70)

# ==============================
# 5. Scrape All Pages
# ==============================

all_products = []

for page in range(
    1,
    total_pages + 1
):

    print("\n")
    print("=" * 70)
    print(f"PAGE {page}/{total_pages}")
    print("=" * 70)

    if page == 1:
        url = BASE_URL
    else:
        url = f"{BASE_URL}?page={page}"

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=30
        )

        response.raise_for_status()

        # Display FULL HTML
        print(response.text)

        # Parse HTML
        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        # Find Products
        products = soup.find_all(
            "a",
            class_="link-product-variant"
        )

        page_products = []

        for product in products:

            data = product.get(
                "x-labels-data"
            )

            if not data:
                continue

            try:

                product_data = json.loads(
                    data
                )

                product_info = {
                    "page": page,

                    "product_id":
                        product_data.get("id"),

                    "name":
                        product_data.get("title"),

                    "price":
                        product_data.get("price"),

                    "old_price":
                        product_data.get(
                            "compare_at_price"
                        ),

                    "available":
                        product_data.get(
                            "available"
                        ),

                    "quantity":
                        product_data.get("qty"),

                    "price_with_currency":
                        product_data.get(
                            "price_with_currency"
                        ),

                    "product_url":
                        "https://dream2000.com"
                        + product.get(
                            "href",
                            ""
                        )
                }

                page_products.append(
                    product_info
                )

            except json.JSONDecodeError:
                continue

        all_products.extend(
            page_products
        )

        print(
            "\nHTML processed successfully."
        )

        print(
            f"Products extracted from page "
            f"{page}: {len(page_products)}"
        )

        time.sleep(1)

    except requests.RequestException as e:

        print(
            f"Error while scraping page "
            f"{page}: {e}"
        )

        continue

# ==============================
# 6. Create DataFrame
# ==============================

df = pd.DataFrame(
    all_products
)

# ==============================
# 7. Remove Duplicate Products
# ==============================

if (
    not df.empty
    and "product_id" in df.columns
):

    df = df.drop_duplicates(
        subset="product_id"
    )

# ==============================
# 8. Save CSV
# ==============================

csv_file = "dream2000_products.csv"

df.to_csv(
    csv_file,
    index=False,
    encoding="utf-8-sig"
)

# ==============================
# 9. Final Results
# ==============================

print("\n")
print("=" * 70)
print("FINAL RESULTS")
print("=" * 70)

print(
    f"Total pages scraped: "
    f"{total_pages}"
)

print(
    f"Total unique products: "
    f"{len(df)}"
)

print(
    f"CSV file: {csv_file}"
)

if len(df) >= 1000:

    print(
        "\nSUCCESS! "
        "The CSV file contains "
        "at least 1000 rows."
    )

else:

    print(
        "\nWARNING! "
        "The CSV file contains "
        "less than 1000 rows."
    )

print("=" * 70)

# ==============================
# 10. Close Terminal Output File
# ==============================

terminal_file.close()