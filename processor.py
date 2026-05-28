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