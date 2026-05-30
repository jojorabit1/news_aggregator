# main.py
from collectors import fetch_feed, SOURCES
from processor import deduplicate, filter_articles, rank_articles
from summarizer import summarize_news

# Artikel von allen Quellen holen
all_articles = []

for source in SOURCES:
    articles = fetch_feed(source)
    all_articles.extend(articles)

print(f"Gesamt: {len(all_articles)} Artikel")

# Duplikate entfernen
unique = deduplicate(all_articles)

# Filtern
filtered = filter_articles(unique)

# Ranking
top_articles = rank_articles(filtered, top_n=5)

print("Sende Top-Artikel an Claude...")

# Zusammenfassung
bericht = summarize_news(top_articles)

print("\n--- TAGESBERICHT ---\n")
print(bericht)