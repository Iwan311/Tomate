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
