# processor.py
# Verantwortlich für: Deduplication und Ranking der Artikel

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Ab diesem Wert gelten zwei Artikel als Duplikat
THRESHOLD = 0.75


def deduplicate(articles: list) -> list:
    """
    Entfernt doppelte Artikel anhand von TF-IDF Cosine Similarity.
    Gibt eine bereinigte Liste ohne Duplikate zurück.
    """
    if not articles:
        return []

    # Titel aller Artikel als Liste extrahieren
    titles = [article["title"] for article in articles]

    # TF-IDF Vektoren berechnen
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(titles)

    # Cosine Similarity zwischen allen Artikeln berechnen
    similarity_matrix = cosine_similarity(tfidf_matrix)

    # Duplikate markieren
    seen = set()
    unique_articles = []

    for i, article in enumerate(articles):
        if i in seen:
            continue

        unique_articles.append(article)

        # Alle ähnlichen Artikel als Duplikat markieren
        for j in range(i + 1, len(articles)):
            if similarity_matrix[i][j] >= THRESHOLD:
                seen.add(j)

    return unique_articles

def filter_articles(articles: list) -> list:
    """
    Entfernt unerwünschte Artikel anhand von Schlüsselwörtern im Titel.
    """
    # Titel die diese Begriffe enthalten werden herausgefiltert
    blocklist = [
        "nachrichten aus",
        "wetter",
        "livestream",
        "programm",
        "debatte zur",
        "debatte zum",
        "vereinbarte debatte",
        "nachrichtenstudio",
        "liveblog",
    ]

    filtered = []
    for article in articles:
        title_lower = article["title"].lower()

        # Prüfe, ob ein Blocklistbegriff im Titel vorkommt
        blocked = any(term in title_lower for term in blocklist)

        if not blocked:
            filtered.append(article)

    return filtered


def rank_articles(articles: list, top_n: int = 10) -> list:
    """
    Bewertet Artikel nach Relevanz und gibt die
    Top-N Artikel sortiert zurück.
    """
    if not articles:
        return []

    # Titel extrahieren
    titles = [article["title"] for article in articles]

    # TF-IDF und Similarity berechnen
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(titles)
    similarity_matrix = cosine_similarity(tfidf_matrix)

    # Score für jeden Artikel berechnen
    for i, article in enumerate(articles):

        # Kriterium 1: source_count
        # Wie viele andere Artikel sind ähnlich?
        source_count = sum(
            1 for j in range(len(articles))
            if i != j and similarity_matrix[i][j] >= 0.3
        )

        # Kriterium 2: position
        # Artikel weiter oben im Feed = wichtiger
        position_score = 1 / (i + 1)

        # Gesamtscore berechnen
        article["score"] = (source_count * 0.7) + (position_score * 0.3)

    # Nach Score sortieren - höchster zuerst
    ranked = sorted(articles, key=lambda x: x["score"], reverse=True)

    return ranked[:top_n]