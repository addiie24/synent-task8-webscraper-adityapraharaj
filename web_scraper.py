import requests
from bs4 import BeautifulSoup
import csv


def scrape_books():
    url = "https://books.toscrape.com/"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch books.")
        return
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    with open("books.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price"])
        print("\n--- Books ---\n")
        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text

            writer.writerow([title, price])

            print(f"{title} | {price}")
    print("\nSaved to books.csv")

def scrape_quotes():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch quotes.")
        return
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")
    with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author"])
        print("\n--- Quotes ---\n")
        for quote in quotes:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            writer.writerow([text, author])
            print(f"{author}: {text}")
    print("\nSaved to quotes.csv")

def scrape_news():
    url = "https://www.python.org/blogs/"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch news.")
        return
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = soup.find_all("h2")
    with open("news.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Headline"])
        print("\n--- Headlines ---\n")
        for headline in headlines:
            text = headline.get_text(strip=True)
            if text:
                writer.writerow([text])
                print(text)
    print("\nSaved to news.csv")

def menu():
    while True:
        print("\n===== MULTI-PURPOSE WEB SCRAPER =====")
        print("1. Scrape Books")
        print("2. Scrape Quotes")
        print("3. Scrape News Headlines")
        print("4. Scrape All")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            scrape_books()
        elif choice == "2":
            scrape_quotes()
        elif choice == "3":
            scrape_news()
        elif choice == "4":
            print("\nScraping all sources...\n")
            scrape_books()
            scrape_quotes()
            scrape_news()
            print("\nAll data scraped successfully!")
        elif choice == "5":
            print("Thank you for using the scraper.")
            break
        else:
            print("Invalid choice.")
menu()