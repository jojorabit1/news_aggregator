# main.py
from collectors import fetch_feed, SOURCES
from processor import deduplicate, filter_articles, rank_articles
from summarizer import summarize_news
from formatter import print_report
from reporter import save_html_report

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
top_articles = rank_articles(filtered, top_n=10)

# Zusammenfassung
summary = summarize_news(top_articles)

# Terminal Report
print_report(top_articles, summary)

# HTML Report speichern
dateiname = save_html_report(top_articles, summary)
print(f"\n✅ HTML Report gespeichert: {dateiname}")