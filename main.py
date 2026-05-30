# main.py
# Einstiegspunkt des Programms - hier wird alles zusammengeführt

from collectors import fetch_feed, SOURCES
from processor import deduplicate, filter_articles, rank_articles
from summarizer import summarize_news
from formatter import print_report

# Artikel von allen Quellen holen
all_articles = []

for source in SOURCES:
    articles = fetch_feed(source)
    all_articles.extend(articles)

# Duplikate entfernen
unique = deduplicate(all_articles)

# Filtern
filtered = filter_articles(unique)

# Ranking
top_articles = rank_articles(filtered, top_n=5)

# Zusammenfassung
summary = summarize_news(top_articles)

# Report ausgeben
print_report(top_articles, summary)