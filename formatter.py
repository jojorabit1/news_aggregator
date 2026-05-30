# formatter.py
# Verantwortlich für: Formatierte Ausgabe des Tagesberichts im Terminal

from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule

# Console Objekt erstellen
console = Console()


def print_report(top_articles: list, summary: str) -> None:
    """
    Gibt den Tagesbericht formatiert im Terminal aus.
    """
    # Datum
    heute = datetime.now().strftime("%d.%m.%Y")

    # Titel
    console.print(Panel(
        f"[bold]TAGESBERICHT {heute}[/bold]",
        style="blue"
    ))

    # Top Artikel
    console.print(Rule("[bold]TOP NACHRICHTEN[/bold]"))

    for i, article in enumerate(top_articles):
        console.print(f"\n[bold]{i+1}. {article['title']}[/bold]")
        console.print(f"   Quelle: [blue]{article['outlet']}[/blue]")
        console.print(f"   Score:  {article['score']:.2f}")

    # Zusammenfassung
    console.print(Rule("[bold]KI-ZUSAMMENFASSUNG[/bold]"))
    console.print(f"\n{summary}\n")