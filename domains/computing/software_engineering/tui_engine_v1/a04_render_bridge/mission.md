# Mission: a04_render_bridge

## Die Objective
Du hast eine Mission gewählt – jetzt musst du sie lesen. In dieser Mission verbindest du den Pfad-Resolver deines CLIs mit dem mächtigen Renderer von Nexus-Shell.

---

## 🏗️ Der Aufbau
Wir nutzen `school path <id>`, um die Datei zu finden, und `nexus-view.sh`, um sie mit Glow (und Mermaid) anzuzeigen.

---

## 🛠️ Die Aufgaben

### 1. Der Pfad-Resolver
Integriere in dein `scripts/launch.sh` (oder ein neues `scripts/view.sh`) den Aufruf:
```bash
MISSION_PATH=$(school path "$MISSION_ID")
```

### 2. Das Rendering
Rufe nun `nexus-view.sh "$MISSION_PATH"` auf. Beachte, dass Nexus-Shell eigene Pfade für seine Bibliotheken nutzt. Du musst eventuell den Pfad zur `lib/nexus-view.sh` absolut angeben.

### 3. Der Mermaid-Test
Finde eine Mission, die ein Mermaid-Diagramm enthält (z.B. in `git_mastery`). Stelle sicher, dass Nexus-Shell das Diagramm korrekt übersetzt und anzeigt.

---

## 🎯 Verifizierungskriterien
- [ ] Die gewählte Mission wird formatiert im Terminal angezeigt.
- [ ] Mermaid-Diagramme werden (bei installiertem `mmdc`) gerendert.
- [ ] Du verstehst, wie man Bash-Skripte über verschiedene Verzeichnisse hinweg sicher aufruft.
