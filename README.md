
<br />
<h3 align="center"><a href="">Spu-UI</a></h3>
    <p align="center">
    Benutzeroberfläsche für den SpuMax.
    </p>
</p>

<!-- TABLE OF CONTENT> -->
## Inhaltsverzeichnis

- [Inhaltsverzeichnis](#Inhaltsverzeichnis)
- [Ordnerstruktur](#Ordnerstruktur)



## Ordnerstruktur
- **main.py**: Die Hauptdatei, hier wird die Anwendung gestartet.

- **README.md**: eine kurze Beschreibung, Installationsanweisungen, etc.

- **requirements.txt**: Eine Datei, die die Abhängigkeiten des Projekts auflistet.
  Abhängigkeiten können mit `pip install -r requirements.txt` installiert werden.

- **ui/**: Enthält alle UI-Dateien, die mit dem Qt Designer erstellt wurden (z. B. mainwindow.ui).

- **src/**: Hier liegen die Quellcodedateien.
  - **\_\_init\_\_.py**: Eine leere Datei, die sicherstellt, dass Python den Ordner als Modul erkennt. 
  - **mainwindow.py**: Die Implementierung der Hauptfensterklasse, in der du die Logik deiner Anwendung platzieren kannst.

- **resources/**: Ordner für Ressourcen.
  - **images/**: Ein Unterordner für Bilder.

- **tests/**: Unit-Tests.
  - **\_\_init\_\_.py**: Eine leere Datei, die sicherstellt, dass Python den Ordner als Modul erkennt. 
  - **test_mainwindow.py**: Beispielhafte Unit-Tests für die mainwindow.py-Datei.
