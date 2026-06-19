import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    with open("books.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(["Title", "Price"])

        print("\nBooks Found:\n")

        for book in books:

            title = book.h3.a["title"]

            price = book.find("p", class_="price_color").text

            writer.writerow([title, price])

            print(f"{title} - {price}")

    print("\nData saved to books.csv")

else:
    print("Failed to fetch website")