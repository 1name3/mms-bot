%25-
<p align="center">
  <img src="Neues%20Projekt.png" alt="MMS Bot Banner" width="800">
</p>

# MMS.ba Auto Writer Bot

Ein einfacher Python-Bot, der automatisch Texte auf der MMS.ba-Website eintippt – ähnlich einer Schreibmaschine.  
Er nutzt Google Chrome zur Automatisierung und hilft dabei, Übungen schneller zu erledigen.

---

## 📋 Inhaltsverzeichnis
- [Status](#status)
- [Funktionen](#funktionen)
- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
  - [Spezielle Hinweise für Windows-Nutzer](#spezielle-hinweise-für-windows-nutzer)
- [Verwendung](#verwendung)
- [Hinweise](#hinweise)
- [Mitwirken](#mitwirken)
- [Lizenz](#lizenz)

---

## 🚧 Status

Dieses Projekt befindet sich aktuell noch in der Entwicklung.  
Der Bot funktioniert bereits in Grundzügen, kann aber noch Fehler verursachen.  
Ich arbeite aktiv an Verbesserungen, neuen Funktionen und einem möglichen Interface!

---

## ✨ Funktionen

- Automatisches Schreiben des benötigten Übungstextes auf MMS.ba
- Einfache Bedienung: Script starten, Lektion und Aufgabe auswählen
- Steuerung und Automatisierung über den Chrome-Browser
- Ideal für Schüler und Nutzer, die den Tippvorgang beschleunigen möchten

---

## 🛠️ Voraussetzungen

- Python 3.x
- Google Chrome installiert
- Passender ChromeDriver
- Python-Bibliothek `selenium`

---

## 📥 Installation

1. Repository klonen oder Dateien herunterladen.
2. Benötigte Python-Bibliothek installieren:
   ```bash
   pip install selenium
   ```
3. ChromeDriver herunterladen:  
   [https://sites.google.com/a/chromium.org/chromedriver/](https://sites.google.com/a/chromium.org/chromedriver/)
4. ChromeDriver:
   - Im selben Verzeichnis wie das Skript speichern **oder**
   - Pfad zum ChromeDriver im Code anpassen.

---

## 🖥️ Spezielle Hinweise für Windows-Nutzer

**Python und Pip Befehle**

- Falls `python` oder `pip` nicht erkannt wird:
  ```bash
  py -m pip install selenium
  ```
  und
  ```bash
  py mms_writer_bot.py
  ```

**ChromeDriver Setup**

- Lade die passende ChromeDriver-Version herunter.
- Lege die `chromedriver.exe` ins gleiche Verzeichnis wie dein Skript.
- Alternativ: Füge den ChromeDriver-Ordner zur Systemumgebungsvariablen `PATH` hinzu:
  - Rechtsklick auf „Dieser PC“ → Eigenschaften → Erweiterte Systemeinstellungen → Umgebungsvariablen → `Path` → Bearbeiten → neuen Ordnerpfad hinzufügen.

**Terminal verwenden**

- CMD oder PowerShell öffnen, dann:
  ```bash
  python mms_writer_bot.py
  ```

---

## 🚀 Verwendung

1. Skript starten:
   ```bash
   python mms_writer_bot.py
   ```
2. Chrome öffnet sich automatisch.
3. Lektion und Aufgabe auswählen.
4. Der Bot beginnt automatisch zu tippen.

---

## ℹ️ Hinweise

- Der Bot ist **nur für Bildungszwecke** entwickelt worden.
- Bitte die Regeln und Nutzungsbedingungen der Website respektieren:  
  [https://mms.baa.at/](https://mms.baa.at/)

---

## 🤝 Mitwirken

Pull Requests, Bug Reports und neue Ideen sind jederzeit willkommen! 🎉  
Einfach das Repository forken, Änderungen machen und einen Merge Request einreichen.

---

## 📄 Lizenz

Dieses Projekt steht unter der [MIT-Lizenz](LICENSE).

---

**Projektfortschritt:**  
![Progress](https://img.shields.io/badge/progress-76red)
