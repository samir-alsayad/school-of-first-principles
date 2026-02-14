# Mission: a01_data_first_cli

## Die Objective
In einem modularen System ist die Logik von der Anzeige getrennt. Dein `school`-CLI soll nicht mehr direkt formatierte Tabellen ausgeben, sondern als **Daten-Provider** für das Nexus-Shell fungieren. In dieser Mission refactorst du das CLI auf **Typer** und fügst Befehle hinzu, die Maschinen-lesbare Daten liefern.

---

## 🏗️ Der Aufbau
Das Ziel ist es, zwei neue Befehle bereitzustellen, die das Nexus-Shell Modul zur Navigation nutzen kann.

---

## 🛠️ Die Aufgaben

### 1. Das Typer-Upgrade
Migriere `src/school/cli.py` von `argparse` zu `Typer`. Verwende Typer-Optionen für `--scope` und `--id`.

### 2. Der Befehl `school list`
Implementiere den Befehl `school list --unlocked`.
- **Eingabe**: Keine (liest `ledger.yaml` und `domains/`).
- **Ausgabe**: Eine flache Liste von Missionen, die der Benutzer aktuell starten kann (alle Voraussetzungen erfüllt).
- **Format**: Jede Zeile eine Mission (z.B. `computing.fundamentals.git_mastery_v1.a01`).

### 3. Der Befehl `school path`
Implementiere den Befehl `school path <mission_id>`.
- **Eingabe**: Die ID einer Mission.
- **Ausgabe**: Der absolute Pfad zur `mission.md` Datei auf deinem System.

---

## 🎯 Verifizierungskriterien
- [ ] `school list --unlocked` liefert eine Liste von Strings zurück.
- [ ] `school path <id>` gibt einen existierenden Dateipfad aus.
- [ ] Das CLI hat keine unnötigen "Lade"-Meldungen in der Standardausgabe (nur saubere Daten).
- [ ] Du verstehst das Prinzip des **Backend/Frontend-Splits** im Terminal-Kontext.
