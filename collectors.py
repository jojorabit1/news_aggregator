import feedparser
import requests
from bs4 import BeautifulSoup


SOURCES = [
    # Politik & Allgemein
    {"name": "ARD Tagesschau", "url": "https://www.tagesschau.de/xml/rss2/", "outlet": "ARD", "category": "Politik"},
    {"name": "ARD Inland", "url": "https://www.tagesschau.de/xml/rss2_inland/", "outlet": "ARD", "category": "Politik"},
    {"name": "ARD Ausland", "url": "https://www.tagesschau.de/xml/rss2_ausland/", "outlet": "ARD", "category": "Politik"},
    {"name": "ZDF heute", "url": "https://www.zdf.de/rss/zdf/nachrichten", "outlet": "ZDF", "category": "Politik"},
    {"name": "Spiegel", "url": "https://www.spiegel.de/schlagzeilen/index.rss", "outlet": "Spiegel", "category": "Politik"},
    {"name": "Zeit Online", "url": "https://newsfeed.zeit.de/all", "outlet": "Zeit", "category": "Politik"},

    # Wirtschaft
    {"name": "ARD Wirtschaft", "url": "https://www.tagesschau.de/xml/rss2_wirtschaft/", "outlet": "ARD", "category": "Wirtschaft"},
    {"name": "Spiegel Wirtschaft", "url": "https://www.spiegel.de/wirtschaft/index.rss", "outlet": "Spiegel", "category": "Wirtschaft"},

    # Sport
    {"name": "Spiegel Sport", "url": "https://www.spiegel.de/sport/index.rss", "outlet": "Spiegel", "category": "Sport"},
    {"name": "SZ Sport", "url": "https://rss.sueddeutsche.de/rss/Sport", "outlet": "SZ", "category": "Sport"},

    # International
    {"name": "BBC News", "url": "https://feeds.bbci.co.uk/news/rss.xml", "outlet": "BBC", "category": "International"},
    {"name": "Reuters", "url": "https://feeds.reuters.com/reuters/topNews", "outlet": "Reuters", "category": "International"},
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
            "category": source["category"],  # ← neu
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