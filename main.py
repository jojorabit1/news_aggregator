# main.py
from collectors import fetch_feed, SOURCES
from processor import deduplicate, rank_articles, filter_articles

# Artikel von allen Quellen holen
all_articles = []

for source in SOURCES:
    articles = fetch_feed(source)
    all_articles.extend(articles)

print(f"Gesamt: {len(all_articles)} Artikel")

# Duplikate entfernen
unique = deduplicate(all_articles)
print(f"Nach Deduplication: {len(unique)} Artikel")

filtered = filter_articles(unique)
print(f"Nach Filter: {len(filtered)} Artikel")

# Zeige Artikel die NICHT gefiltert wurden aber "nachrichten" enthalten
for a in filtered:
    if "nachrichten" in a["title"].lower():
        print(a["title"])

# Ranking
top_articles = rank_articles(filtered, top_n=5)

print("\n--- TOP 5 ARTIKEL DES TAGES ---")
for i, article in enumerate(top_articles):
    print(f"\n{i+1}. {article['title']}")
    print(f"   Quelle: {article['outlet']}")
    print(f"   Score:  {article['score']:.2f}")