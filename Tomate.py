print ("Hallo Boss")
import random


def zufaelliges_rezept():
    rezepte = [
        "Spaghetti mit Tomatensauce",
        "Kartoffelsuppe",
        "Pfannkuchen",
        "Salat mit Joghurtdressing",
        "Pizza Margherita",
        "Lasagne",
        "Gemüsesuppe",
        "Schokoladenkuchen"
    ]

    print("Willkommen im Zufalls-Rezept-Generator!")
    print("Dein Rezeptvorschlag ist:")
    print(random.choice(rezepte))


# Programm starten
if __name__ == "__main__":
    zufaelliges_rezept()
def addition(a, b):
    return a + b

def subtraktion(a, b):
    return a - b

def multiplikation(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Fehler: Division durch Null!"

def taschenrechner():
    print("Willkommen zum Python-Taschenrechner!")
    print("Wähle eine Operation:")
    print("1: Addition")
    print("2: Subtraktion")
    print("3: Multiplikation")
    print("4: Division")

    wahl = input("Gib die Nummer der gewünschten Operation ein (1/2/3/4): ")

    if wahl in ['1', '2', '3', '4']:
        num1 = float(input("Gib die erste Zahl ein: "))
        num2 = float(input("Gib die zweite Zahl ein: "))

        if wahl == '1':
            print(f"Ergebnis: {num1} + {num2} = {addition(num1, num2)}")
        elif wahl == '2':
            print(f"Ergebnis: {num1} - {num2} = {subtraktion(num1, num2)}")
        elif wahl == '3':
            print(f"Ergebnis: {num1} * {num2} = {multiplikation(num1, num2)}")
        elif wahl == '4':
            print(f"Ergebnis: {num1} / {num2} = {division(num1, num2)}")
    else:
        print("Ungültige Auswahl! Bitte starte das Programm erneut.")

# Programm starten
if __name__ == "__main__":
    taschenrechner()


def addiere(a, b):
    return a + b


def subtrahiere(a, b):
    return a - b


def multipliziere(a, b):
    return a * b


def dividiere(a, b):
    if b != 0:
        return a / b
    else:
        return "Fehler: Division durch Null ist nicht erlaubt!"


def rechner():
    print("Willkommen zum Python-Taschenrechner!")
    print("Wähle eine Operation:")
    print("1. Addition (+)")
    print("2. Subtraktion (-)")
    print("3. Multiplikation (*)")
    print("4. Division (/)")

    wahl = input("Gib die Nummer der gewünschten Operation ein (1/2/3/4): ")

    if wahl in ['1', '2', '3', '4']:
        try:
            zahl1 = float(input("Gib die erste Zahl ein: "))
            zahl2 = float(input("Gib die zweite Zahl ein: "))

            if wahl == '1':
                print(f"Ergebnis: {zahl1} + {zahl2} = {addiere(zahl1, zahl2)}")
            elif wahl == '2':
                print(f"Ergebnis: {zahl1} - {zahl2} = {subtrahiere(zahl1, zahl2)}")
            elif wahl == '3':
                print(f"Ergebnis: {zahl1} * {zahl2} = {multipliziere(zahl1, zahl2)}")
            elif wahl == '4':
                print(f"Ergebnis: {zahl1} / {zahl2} = {dividiere(zahl1, zahl2)}")
        except ValueError:
            print("Fehler: Bitte gib gültige Zahlen ein!")
    else:
        print("Ungültige Auswahl. Bitte starte das Programm erneut.")


# Programm starten
if __name__ == "__main__":
    rechner()

import random

def rate_zahl():
    print("Willkommen zum Zahlen-Ratespiel!")
    geheimzahl = random.randint(1, 100)
    versuche = 0

    while True:
        try:
            rate = int(input("Rate die Zahl (zwischen 1 und 100): "))
            versuche += 1

            if rate < geheimzahl:
                print("Zu niedrig! Versuch's nochmal.")
            elif rate > geheimzahl:
                print("Zu hoch! Versuch's nochmal.")
            else:
                print(f"Glückwunsch! Du hast die Zahl {geheimzahl} in {versuche} Versuchen erraten.")
                break
        except ValueError:
            print("Bitte gib eine gültige Zahl ein!")

if __name__ == "__main__":
    rate_zahl()

import random
import string

def passwort_generieren():
    print("Willkommen zum Passwort-Generator!")
    länge = int(input("Wie lang soll das Passwort sein? (z. B. 12): "))

    zeichen = string.ascii_letters + string.digits + string.punctuation
    passwort = ''.join(random.choice(zeichen) for _ in range(länge))
    print(f"Dein generiertes Passwort lautet: {passwort}")

if __name__ == "__main__":
    passwort_generieren()
def todo_liste():
    aufgaben = []

    while True:
        print("\nTo-Do-Liste:")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgaben anzeigen")
        print("3. Aufgabe entfernen")
        print("4. Programm beenden")

        wahl = input("Wähle eine Option (1-4): ")

        if wahl == "1":
            aufgabe = input("Gib eine neue Aufgabe ein: ")
            aufgaben.append(aufgabe)
            print(f"Aufgabe '{aufgabe}' hinzugefügt.")
        elif wahl == "2":
            print("\nDeine Aufgaben:")
            if aufgaben:
                for i, aufgabe in enumerate(aufgaben, 1):
                    print(f"{i}. {aufgabe}")
            else:
                print("Keine Aufgaben vorhanden.")
        elif wahl == "3":
            try:
                nummer = int(input("Welche Aufgabe möchtest du entfernen? (Nummer): "))
                if 1 <= nummer <= len(aufgaben):
                    entfernte_aufgabe = aufgaben.pop(nummer - 1)
                    print(f"Aufgabe '{entfernte_aufgabe}' wurde entfernt.")
                else:
                    print("Ungültige Nummer.")
            except ValueError:
                print("Bitte gib eine gültige Nummer ein.")
        elif wahl == "4":
            print("Programm beendet. Bis bald!")
            break
        else:
            print("Ungültige Auswahl! Bitte wähle erneut.")

if __name__ == "__main__":
    todo_liste()
import time

def countdown(sekunden):
    print(f"Timer gestartet für {sekunden} Sekunden...")
    while sekunden:
        mins, secs = divmod(sekunden, 60)
        timer = f'{mins:02}:{secs:02}'
        print(timer, end="\r")
        time.sleep(1)
        sekunden -= 1

    print("Zeit abgelaufen!")

if __name__ == "__main__":
    dauer = int(input("Gib die Zeit in Sekunden ein: "))
    countdown(dauer)
def quiz():
    punkte = 0
    fragen = [
        {"frage": "Was ist die Hauptstadt von Deutschland?", "antwort": "Berlin"},
        {"frage": "Wieviel ist 5 + 5?", "antwort": "10"},
        {"frage": "Welche Programmiersprache verwenden wir hier?", "antwort": "Python"}
    ]

    for frage in fragen:
        antwort = input(frage["frage"] + " ")
        if antwort.lower() == frage["antwort"].lower():
            print("Richtig!")
            punkte += 1
        else:
            print(f"Falsch! Die richtige Antwort ist: {frage['antwort']}")

    print(f"\nDu hast {punkte} von {len(fragen)} Punkten erreicht!")

if __name__ == "__main__":
    quiz()
import random

def stein_schere_papier():
    print("Willkommen bei Stein-Schere-Papier!")
    optionen = ["Stein", "Schere", "Papier"]

    while True:
        spieler_wahl = input("Wähle Stein, Schere oder Papier (oder 'Beenden' zum Aussteigen): ").capitalize()
        if spieler_wahl == "Beenden":
            print("Danke fürs Spielen!")
            break
        if spieler_wahl not in optionen:
            print("Ungültige Wahl. Versuch es nochmal!")
            continue

        computer_wahl = random.choice(optionen)
        print(f"Computer wählt: {computer_wahl}")

        if spieler_wahl == computer_wahl:
            print("Unentschieden!")
        elif (spieler_wahl == "Stein" and computer_wahl == "Schere") or \
             (spieler_wahl == "Schere" and computer_wahl == "Papier") or \
             (spieler_wahl == "Papier" and computer_wahl == "Stein"):
            print("Du gewinnst!")
        else:
            print("Computer gewinnt!")

if __name__ == "__main__":
    stein_schere_papier()
def einheiten_umrechner():
    print("Willkommen beim Einheiten-Umrechner!")
    print("1. Kilometer zu Meilen")
    print("2. Celsius zu Fahrenheit")
    print("3. Kilogramm zu Pfund")

    wahl = input("Wähle eine Option (1/2/3): ")

    if wahl == "1":
        km = float(input("Gib die Anzahl der Kilometer ein: "))
        meilen = km * 0.621371
        print(f"{km} Kilometer sind {meilen:.2f} Meilen.")
    elif wahl == "2":
        celsius = float(input("Gib die Temperatur in Celsius ein: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C sind {fahrenheit:.2f}°F.")
    elif wahl == "3":
        kg = float(input("Gib das Gewicht in Kilogramm ein: "))
        pfund = kg * 2.20462
        print(f"{kg} Kilogramm sind {pfund:.2f} Pfund.")
    else:
        print("Ungültige Auswahl. Bitte starte das Programm erneut.")

if __name__ == "__main__":
    einheiten_umrechner()
def ist_primzahl(zahl):
    if zahl <= 1:
        return False
    for i in range(2, int(zahl ** 0.5) + 1):
        if zahl % i == 0:
            return False
    return True

def prime_checker():
    zahl = int(input("Gib eine Zahl ein: "))
    if ist_primzahl(zahl):
        print(f"{zahl} ist eine Primzahl.")
    else:
        print(f"{zahl} ist keine Primzahl.")

if __name__ == "__main__":
    prime_checker()
def bmi_rechner():
    print("Willkommen beim BMI-Rechner!")
    gewicht = float(input("Gib dein Gewicht in Kilogramm ein: "))
    größe = float(input("Gib deine Größe in Metern ein: "))

    bmi = gewicht / (größe ** 2)
    print(f"Dein BMI ist: {bmi:.2f}")

    if bmi < 18.5:
        print("Untergewicht")
    elif 18.5 <= bmi < 24.9:
        print("Normalgewicht")
    elif 25 <= bmi < 29.9:
        print("Übergewicht")
    else:
        print("Adipositas")

if __name__ == "__main__":
    bmi_rechner()
def reisekosten_rechner():
    print("Willkommen beim Reisekostenrechner!")
    entfernung = float(input("Gib die Entfernung in Kilometern ein: "))
    verbrauch = float(input("Gib den Verbrauch deines Autos (Liter pro 100 km) ein: "))
    spritpreis = float(input("Gib den aktuellen Spritpreis pro Liter ein: "))

    kosten = (entfernung / 100) * verbrauch * spritpreis
    print(f"Die Gesamtkosten für die Reise betragen: {kosten:.2f} Euro.")

if __name__ == "__main__":
    reisekosten_rechner()
def fibonacci(bis):
    a, b = 0, 1
    print("Fibonacci-Folge:")
    while a <= bis:
        print(a, end=" ")
        a, b = b, a + b
    print()

if __name__ == "__main__":
    grenze = int(input("Gib die maximale Zahl für die Fibonacci-Folge ein: "))
    fibonacci(grenze)
