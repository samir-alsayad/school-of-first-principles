# Mission: a03_mission_navigator

## Die Objective
Ein Navigator ist nutzlos, wenn man nicht wählen kann, wohin man geht. In dieser Mission baust du einen interaktiven **Mission Selector** mit `fzf`, der die Daten von deinem `school`-CLI nutzt.

---

## 🏗️ Der Aufbau
Wir nutzen das Pipe-Prinzip: `school list` liefert die Namen -> `fzf` lässt dich wählen -> das Ergebnis wird gespeichert.

---

## 🛠️ Die Aufgaben

### 1. Der FZF-Bridge
Erstelle ein Skript `scripts/navigator.sh`. 
Verwende darin:
```bash
MISSION_ID=$(school list --unlocked | fzf --prompt="Wähle deine Mission> ")
```

### 2. Visuelle Rückmeldung
Nutze `gum` (falls in Nexus installiert) oder einfache ANSI-Farben, um die Auswahl zu bestätigen.
```bash
if [[ -n "$MISSION_ID" ]]; then
    echo -e "\033[1;32mMissions-Start: $MISSION_ID\033[0m"
fi
```

### 3. Integration in den Lifecycle
Sorge dafür, dass nach der Auswahl die gewählte ID in eine temporäre Datei (z.B. `/tmp/nexus_academy/current_mission`) geschrieben wird.

---

## 🎯 Verifizierungskriterien
- [ ] Das Skript öffnet ein `fzf` Menü mit deinen echten Missionen.
- [ ] Nach der Auswahl wird die ID korrekt ausgegeben oder gespeichert.
- [ ] Du kannst erklären, warum `fzf` besser für die Navigation geeignet ist als ein statisches Menü.
- [ ] Du beherrscht die CLI-Pipe zwischen Python (`school`) und Shell (`fzf`).
