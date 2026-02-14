# Mission: a06_academy_layout

## Die Objective
Dies ist die Krönung deines TUI-Projekts. Du baust die **Sovereign Academy Composition**. Ein spezielles Pane-Layout, das deinen Navigator, deine Dokumentation und dein Terminal in einem festen, unzerstörbaren Arbeitsplatz vereint.

---

## 🏗️ Der Aufbau
Wir nutzen das JSON-basierte Layout-System von Nexus-Shell (`compositions/`), um die Panes perfekt anzuordnen.

---

## 🛠️ Die Aufgaben

### 1. Die Komposition
Erstelle die Datei `compositions/academy.json` in deinem Nexus-Shell Repository.
Definiere ein Layout mit drei Hauptbereichen:
- **Oben (20%)**: Der Mission Navigator (`scripts/navigator.sh`).
- **Mitte (50%)**: Der Render-Daemon (zeigt die `mission.md` an).
- **Unten (30%)**: Ein interaktives Terminal zum Arbeiten.

### 2. Integration
Sorge dafür, dass der Befehl `nexus --composition academy` dein individuelles Layout lädt.

### 3. Der Sovereign Flow
Teste den kompletten Workflow:
1. Wähle eine Mission im Navigator.
2. Lies die Anweisungen im Render-Pane.
3. Löse die Aufgabe im Terminal.
4. Schließe die Mission ab (automatische Aktualisierung).

---

## 🎯 Verifizierungskriterien
- [ ] Das Layout lädt alle drei Bereiche beim Start korrekt.
- [ ] Die Navigation im Navigator aktualisiert das Render-Pane.
- [ ] Du hast eine voll funktionsfähige, eigene Lernumgebung geschaffen.
- [ ] Du kannst erklären, wie Composition-Files die "Physicality" deines digitalen Arbeitsplatzes definieren.
