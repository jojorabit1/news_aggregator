# main.py
from collectors import fetch_feed, SOURCES
from processor import deduplicate, filter_articles, rank_articles, group_by_category
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

# Nach Kategorien gruppieren
categories = group_by_category(filtered)

# Pro Kategorie: Top 3 Artikel
top_articles = []
for category, articles in categories.items():
    ranked = rank_articles(articles, top_n=3)
    top_articles.extend(ranked)

# Zusammenfassung
summary = summarize_news(top_articles)

# Terminal Report
print_report(top_articles, summary)

# HTML Report speichern
dateiname = save_html_report(top_articles, summary)
print(f"\n✅ HTML Report gespeichert: {dateiname}")