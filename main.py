# main.py
from collectors import fetch_feed, scrape_article, SOURCES

# ersten Artikel von ARD holen
articles = fetch_feed(SOURCES[0])


first_link = articles[0]["link"]
print("Link:", first_link)
print("---")

# Artikeltext scrapen
text = scrape_article(first_link)

# Ersten 500 Zeichen ausgeben
print(text[:500])
