import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://books.toscrape.com/"

def scrape_books():
    books = []
    url = BASE_URL
    response = requests.get(url)

    if response.status_code != 200:
        print("Site fora do ar!")
        exit()

    if url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for book in soup.select(".product_pod"):
            
            title = book.h3.a["title"]
            price = book.select_one(".price_color").text.strip()

            books.append({
                "Titulo": title,
                "Preço": price
            })
        
    df = pd.DataFrame(books)
    df.to_csv("data/books.csv", index=False, encoding="utf-8")
    
    print(f"{len(books)} livros salvos na planilha")



if __name__ == "__main__":
    scrape_books()
