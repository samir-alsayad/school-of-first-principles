# Mission: a01_typer_transition

## Das Ziel
Moderne CLI-Tools müssen ergonomisch und leicht erweiterbar sein. Während `argparse` der Standard ist, wird es unhandlich, sobald die Anzahl der Unterbefehle wächst. In dieser Mission wirst du das bestehende `school`-CLI auf **Typer** umstellen. Dies ist der erste Schritt beim Bau unserer TUI-Engine, da Typer perfekt mit der Rendering-Power von Rich integriert.

---

## 🏗️ Der Zustand der Academy
Das aktuelle CLI befindet sich in `src/school/cli.py` und verwendet ein klassisches `argparse`-Setup. Dein Ziel ist es, dies durch eine Typer-Anwendung zu ersetzen, während die Abwärtskompatibilität für den `status`-Befehl erhalten bleibt.

---

## 🛠️ Die Aufgaben

### 1. Der Prototyp
Erstelle eine temporäre Experimentierdatei `workbench/typer_lab.py`, um die Typer-Syntax zu testen.
```python
import typer

app = typer.Typer()

@app.command()
def status(
    scope: str = typer.Option("total", help="Umfang des Fortschritts"),
    id: str = typer.Option(None, help="Spezifische Modul- oder Kampagnen-ID")
):
    print(f"Prüfe Status für: {scope}")
    if id:
        print(f"Ziel-ID: {id}")

if __name__ == "__main__":
    app()
```

### 2. Der Refactor
Passe nun `src/school/cli.py` an.
-   Importiere `typer`.
-   Initialisiere `app = typer.Typer(help="School CLI - Die souveräne Schnittstelle")`.
-   Migriere die `cmd_status`-Logik in einen `@app.command()`.

> [!IMPORTANT]
> Behalte die Importe von `from .commands import cmd_status` bei, aber kapsele den Aufruf in einer typsicheren Funktion.

### 3. Verifizierung
Überprüfe, ob der `school`-Befehl noch wie erwartet funktioniert:
```bash
# Sicherstellen, dass der Einstiegspunkt noch funktioniert
PYTHONPATH=src python3 -m school status --scope total
```

---

## 🎯 Verifizierungskriterien
- [ ] `school --help` zeigt ein sauberes, automatisch generiertes Hilfemenü.
- [ ] Das Ausführen von `school status` ohne Argumente verwendet standardmäßig den Umfang `total`.
- [ ] Du kannst erklären, warum Typers Verwendung von **Type Hints** `(scope: str = ...)` der stringbasierten Konfiguration von `argparse` überlegen ist.
- [ ] Das CLI verwendet nun einen Standard-Einstiegspunkt, den wir leicht um `read`- und `browse`-Befehle erweitern können.
