# summarizer.py
# Verantwortlich für: Zusammenfassung der Top-Artikel mit Groq API

import os
from dotenv import load_dotenv
from groq import Groq

# .env Datei laden
load_dotenv()

# Groq Client erstellen
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def summarize_news(articles: list) -> str:
    """
    Schickt die Top-Artikel an Groq und gibt
    einen kompakten Tagesbericht zurück.
    """
    # Artikel als Text aufbereiten
    artikel_text = ""
    for i, article in enumerate(articles):
        artikel_text += f"{i+1}. {article['title']}\n"
        artikel_text += f"   Quelle: {article['outlet']}\n"
        artikel_text += f"   Zusammenfassung: {article['summary']}\n\n"

    # Prompt
    prompt = f"""Du bist ein professioneller Nachrichtenredakteur.
Fasse die folgenden Top-Nachrichten des Tages in einem kompakten,
sachlichen Tagesbericht auf Deutsch zusammen.

Nachrichten:
{artikel_text}

Schreibe einen fließenden Tagesbericht in 150-200 Wörtern."""

    # API Anfrage
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content