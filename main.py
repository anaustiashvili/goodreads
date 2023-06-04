import requests
from bs4 import BeautifulSoup
import time

url = "https://www.goodreads.com/search"
delay = 16

for i in range(1, 6):
    dict = {
        "q": "fiction",
        "page": i
    }

    response = requests.get(url, params=dict)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        books = soup.find_all("tr", itemtype="http://schema.org/Book")

        for book in books:
            title_element = book.find("a", class_="bookTitle")
            author_element = book.find("a", class_="authorName")

            if title_element and author_element:
                title = title_element.text.strip()
                author = author_element.text.strip()

                print(f"Book,Author: {title}({author})")

        time.sleep(delay)
    else:
        print("Request failed for page", i)