# Mission: a02_nexus_module_setup

## Die Objective
Jetzt, wo dein `school`-CLI Daten liefern kann, ist es an der Zeit, das **Nexus-Shell** zu erweitern. In dieser Mission baust du das Grundgerüst für dein eigenes Nexus-Modul. 

---

## 🏗️ Der Aufbau
Ein Nexus-Modul ist ein Verzeichnis in `modules/`, das eine bestimmte Struktur und ein `manifest.json` besitzt.

---

## 🛠️ Die Aufgaben

### 1. Die Modul-Struktur
Erstelle das Verzeichnis `modules/academy` in deinem Nexus-Shell Repository.
Lege darin folgende Struktur an:
- `manifest.json` (Die Modul-Beschreibung)
- `scripts/` (Deine Shell-Skripte)
- `install.sh` (Optional: Installation von Abhängigkeiten)

### 2. Das Manifest
Fülle die `manifest.json` mit den Basis-Informationen:
```json
{
  "name": "academy",
  "version": "1.0.0",
  "description": "The Sovereign Scholar Station",
  "author": "Scholar",
  "dependencies": ["glow", "fzf"]
}
```

### 3. Der erste Test
Erstelle ein Skript `scripts/launch.sh`, das einfach nur `echo "Academy Station Initialized"` ausgibt. Versuche, dieses Skript über die Nexus-Shell Befehlszeile (`:a` oder `Alt+Shift+A`) aufrufbar zu machen.

---

## 🎯 Verifizierungskriterien
- [ ] Der Ordner `modules/academy` existiert.
- [ ] `manifest.json` ist ein gültiges JSON.
- [ ] Du kannst das Academy-Modul innerhalb von Nexus "sehen".
- [ ] Du verstehst, wie Nexus-Shell Module entdeckt und registriert.
