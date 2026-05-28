# main.py
from collectors import fetch_feed, scrape_article, SOURCES
from processor import deduplicate

# Artikel von ALLEN Quellen holen
all_articles = []

for source in SOURCES:
    articles = fetch_feed(source)
    print(f"{source['name']}: {len(articles)} Artikel")  # ← neu
    all_articles.extend(articles)

print(f"Vor Deduplication: {len(all_articles)} Artikel")

#Duplikate entfernen
unique = deduplicate(all_articles)

print(f"Nach Deduplication: {len(unique)} Artikel")