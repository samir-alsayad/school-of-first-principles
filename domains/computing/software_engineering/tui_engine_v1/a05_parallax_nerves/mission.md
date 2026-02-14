# Mission: a05_parallax_nerves

## Die Objective
Ein statisches Interface ist langweilig. In dieser Mission baust du das "Nervensystem" deiner Academy. Wenn du eine Mission abschließt, soll dein Interface das sofort bemerken, ohne dass du es neu starten musst. Wir nutzen dafür den **Parallax Event Bus**.

---

## 🏗️ Der Aufbau
Wir nutzen `nxs-event`, um Nachrichten zwischen deinem Python-Kern (`school`) und dem Nexus-Frontend zu senden.

---

## 🛠️ Die Aufgaben

### 1. Das Event-Server Setup
Stelle sicher, dass der Parallax Event-Bus läuft. Er wird normalerweise beim Start von Nexus-Shell im Hintergrund gestartet. Die Socket-Datei befindet sich meist unter `/tmp/nexus_$USER/$PROJECT/bus.sock`.

### 2. Senden von Events (Backend)
Erweitere deinen `school verify` Befehl in Python. Sobald eine Mission erfolgreich verifiziert wurde, soll er ein Bash-Kommando (oder Python-Socket-Aufruf) auslösen:
```bash
nxs-event publish ACADEMY_EVENT '{"action":"mission_completed", "id":"..."}'
```

### 3. Empfangen von Events (Frontend)
Erstelle ein Skript `scripts/listener.sh`, das auf diese Events wartet und den Navigator (`scripts/navigator.sh`) neu zeichnet:
```bash
nxs-event subscribe ACADEMY_EVENT | while read -r event; do
    # Logik zum Neuladen des Menüs
done
```

---

## 🎯 Verifizierungskriterien
- [ ] Du kannst ein Test-Event über die Konsole senden und dein Listener reagiert darauf.
- [ ] `school verify` löst automatisch ein Update im Navigator aus.
- [ ] Du verstehst den Unterschied zwischen **Polling** (Abfragen) und **Event-Driven** (Ereignis-gesteuert) Architektur.
- [ ] Du hast das Konzept des **IPC (Inter-Process Communication)** für Sovereign TUIs gemeistert.
