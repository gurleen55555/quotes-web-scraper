import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://quotes.toscrape.com/page/1/"

res = requests.get(URL)
soup = BeautifulSoup(res.text, "lxml")

all_quotes = soup.select("div.quote")

life_quotes = []

for q in all_quotes:
    tags = []

    for tag in q.select(".tags .tag"):
        tags.append(tag.get_text())

    if "life" in tags:
        text = q.select_one("span.text").get_text()
        author = q.select_one("small.author").get_text()

        life_quotes.append([text, author])

# Convert to CSV
df = pd.DataFrame(life_quotes, columns=["Quote", "Author"])
df.to_csv("life_quotes.csv", index=False)

print("Scraping completed!")