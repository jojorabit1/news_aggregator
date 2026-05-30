import feedparser
import requests
from bs4 import BeautifulSoup


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
    {
        "name": "Spiegel",
        "url": "https://www.spiegel.de/schlagzeilen/index.rss",
        "outlet": "Spiegel",
    },
    {
        "name": "Zeit Online",
        "url": "https://newsfeed.zeit.de/all",
        "outlet": "Zeit",
    },
    {
        "name": "Süddeutsche Zeitung",
        "url": "https://rss.sueddeutsche.de/alles",
        "outlet": "SZ",
    },
    {
        "name": "n-tv",
        "url": "https://www.n-tv.de/rss",
        "outlet": "n-tv",
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

def scrape_article(url: str) -> str:
    """
    Ruft die Website eines Artikels ab und extrahiert
    den reinen Fließtext ohne HTML-Tags.
    """
    try:
        # Website abrufen
        response = requests.get(url, timeout=10)

        # HTML parsen
        soup = BeautifulSoup(response.text, "lxml")

        #Artikeltext extrahieren
        article = soup.find("article")

        if article:
            return article.get_text(separator=" ", strip=True)
        else:
            return ""

    except Exception as e:
        # Bei Fehler: leeren String zurückgeben statt abstürzen
        print(f"Fehler beim Scraping: {e}")
        return ""