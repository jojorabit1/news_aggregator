# reporter.py
# Verantwortlich für: HTML-Report erstellen und speichern

from datetime import datetime


def save_html_report(top_articles: list, summary: str) -> str:
    """
    Erstellt einen HTML-Tagesbericht und speichert ihn als Datei.
    Gibt den Dateinamen zurück.
    """
    heute = datetime.now().strftime("%d.%m.%Y")
    dateiname = f"tagesbericht_{datetime.now().strftime('%Y%m%d')}.html"

    # Artikel als HTML aufbereiten
    artikel_html = ""
    for i, article in enumerate(top_articles):
        artikel_html += f"""
        <div class="article">
            <h3>{i+1}. {article['title']}</h3>
            <p class="meta">
                Quelle: <span class="outlet">{article['outlet']}</span>
                &nbsp;|&nbsp;
                Score: {article['score']:.2f}
            </p>
            <a href="{article['link']}" target="_blank">Artikel lesen →</a>
        </div>
        """

    # HTML zusammenbauen
    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Tagesbericht {heute}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 0 20px;
            background: #f5f5f5;
            color: #333;
        }}
        h1 {{
            background: #1a1a2e;
            color: white;
            padding: 20px;
            border-radius: 8px;
        }}
        h2 {{
            border-bottom: 2px solid #1a1a2e;
            padding-bottom: 8px;
            margin-top: 40px;
        }}
        .article {{
            background: white;
            padding: 16px;
            margin: 12px 0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .article h3 {{
            margin: 0 0 8px 0;
        }}
        .meta {{
            color: #666;
            font-size: 0.9em;
        }}
        .outlet {{
            color: #1a1a2e;
            font-weight: bold;
        }}
        a {{
            color: #e94560;
            text-decoration: none;
        }}
        .summary {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            line-height: 1.7;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
    </style>
</head>
<body>
    <h1>📰 Tagesbericht {heute}</h1>

    <h2>Top Nachrichten</h2>
    {artikel_html}

    <h2>KI-Zusammenfassung</h2>
    <div class="summary">
        {summary.replace(chr(10), '<br>')}
    </div>
</body>
</html>"""

    # Datei speichern
    with open(dateiname, "w", encoding="utf-8") as f:
        f.write(html)

    return dateiname