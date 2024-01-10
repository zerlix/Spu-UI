
<br />
<h3 align="center"><a href="">Spu-UI</a></h3>
    <p align="center">
    Benutzeroberfläsche für den SpuMax.
    </p>
</p>

<!-- TABLE OF CONTENT> -->
## Inhaltsverzeichnis

- [Inhaltsverzeichnis](#Inhaltsverzeichnis)
- [Kompilieren des UI Files](#Kompilieren)
- [Ordnerstruktur](#Ordnerstruktur)


## Kompilieren des UI Files
Die UI Dateien aus dem Verzeichnis ./ui können mit dem script ui_compile.py kompiliert werden<br />

`python ui_compile.pyi`      

## Ordnerstruktur
- **main.py**: Die Hauptdatei, hier wird die Anwendung gestartet.

- **README.md**: eine kurze Beschreibung, Installationsanweisungen, etc.

- **requirements.txt**: Eine Datei, die die Abhängigkeiten des Projekts auflistet.<br />
  Abhängigkeiten können mit `pip install -r requirements.txt` installiert werden.

- **ui/**: Enthält alle UI-Dateien, die mit dem Qt Designer erstellt wurden (z. B. mainwindow.ui).

- **src/**: Hier liegen die Quellcodedateien.
  - **\_\_init\_\_.py**: Eine leere Datei, die sicherstellt, dass Python den Ordner als Modul erkennt. 

- **resources/**: Ordner für Ressourcen.
  - **images/**: Ein Unterordner für Bilder.

- **tests/**: Unit-Tests.
  - **\_\_init\_\_.py**: Eine leere Datei, die sicherstellt, dass Python den Ordner als Modul erkennt. 
  - **test_mainwindow.py**: Beispielhafte Unit-Tests für die mainwindow.py-Datei.
