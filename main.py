# main.py
# Einstiegspunkt des Programms - hier wird alles zusammengeführt

from collectors import fetch_feed, SOURCES

articles = fetch_feed(SOURCES[0])
print(articles[0].keys())


for article in articles[:3]:
    print(article["title"])
    print(article["link"])
    print("---")
