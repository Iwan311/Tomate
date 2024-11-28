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
