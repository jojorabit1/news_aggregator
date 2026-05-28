import feedparser


SOURCES = [
    {
        "name": "ARD Tagesschau",
        "url": "https://www.tagesschau.de/xml/rss2/",
        "outlet": "ARD",
    },
    {
        "name": "ZDF heute",
        "url": "https://www.zdf.de/rss/zdf/nachrichten",
        "outlet": "ZDF",
    },
]

def fetch_feed(source: dict) -> list:
    """
    Ruft einen einzelnen RSS-Feed ab und gibt eine Liste
    von Artikeln als Dictionaries zurück.
    """
    feed = feedparser.parse(source["url"])
    articles = []  # Ergebnisliste, wird Schritt für Schritt befüllt

    for entry in feed.entries:
        # Nur relevante Felder extrahieren, Rest ignorieren
        article = {
            "title":   entry.get("title", ""),
            "summary": entry.get("summary", ""),
            "link":    entry.get("link", ""),
            "outlet":  source["outlet"],
        }
        articles.append(article)

    return articles