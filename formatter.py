# formatter.py
# Verantwortlich für: Formatierte Ausgabe des Tagesberichts im Terminal

from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule

console = Console()

# Emoji pro Kategorie
CATEGORY_ICONS = {
    "Politik":       "🏛️",
    "Wirtschaft":    "💰",
    "Sport":         "🏆",
    "International": "🌍",
    "Sonstiges":     "📰",
}


def print_report(top_articles: list, summary: str) -> None:
    """
    Gibt den Tagesbericht formatiert im Terminal aus.
    """
    heute = datetime.now().strftime("%d.%m.%Y")

    # Titel
    console.print(Panel(
        f"[bold]TAGESBERICHT {heute}[/bold]",
        style="blue"
    ))

    # Artikel nach Kategorie gruppieren
    categories = {}
    for article in top_articles:
        cat = article.get("category", "Sonstiges")
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(article)

    # Pro Kategorie ausgeben
    for category, articles in categories.items():
        icon = CATEGORY_ICONS.get(category, "📰")
        console.print(Rule(f"[bold]{icon} {category}[/bold]"))

        for i, article in enumerate(articles):
            console.print(f"\n[bold]{i+1}. {article['title']}[/bold]")
            console.print(f"   Quelle: [blue]{article['outlet']}[/blue]")

    # Zusammenfassung
    console.print(Rule("[bold]🤖 KI-ZUSAMMENFASSUNG[/bold]"))
    console.print(f"\n{summary}\n")