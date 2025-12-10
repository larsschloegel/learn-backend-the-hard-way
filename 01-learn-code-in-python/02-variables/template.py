import os
import argparse

def create_project(path_or_name):
    # Prüfen, ob absoluter Pfad
    if os.path.isabs(path_or_name):
        full_path = path_or_name
    else:
        # relativer Pfad → im aktuellen Arbeitsverzeichnis anlegen
        full_path = os.path.join(os.getcwd(), path_or_name)

    # Ordner erstellen
    os.makedirs(full_path, exist_ok=True)

    # Standard-Dateien
    files = ["i.md", "main_test.py", "main.py", "solution.py"]

    for file in files:
        file_path = os.path.join(full_path, file)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("")  # leer oder Template einfügen

    print(f"Projekt erstellt unter: {full_path}")
    print(f"Erstellte Dateien: {', '.join(files)}")


def main():
    parser = argparse.ArgumentParser(
        description="Erstellt einen Projektordner mit Standarddateien."
    )
    parser.add_argument(
        "path",
        type=str,
        help="Ordnername oder Pfad, in dem das Projekt angelegt werden soll"
    )

    args = parser.parse_args()
    create_project(args.path)


if __name__ == "__main__":
    main()