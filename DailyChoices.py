import time

def dailychoices():
    print("Hey hoi hallo goeie morgen! Ga je nu je bed uit of niet en blijf je nog 10 minuten liggen? Antwoord met: Ja/Nee")
    choice = input()
    if choice.lower() == "ja":
        print("Mooi zo je bent iemand die vroeg zn bed uit gaat.")
    elif choice.lower() == "nee":
        print("Lekker man, nog ff door pitten.")
    else:
        print(choice, "is niet een geldig antwoord.")

time.sleep(1)
def dailychoices2():
    print("Gaan we douchen of alleen wassen? Antwoord met: Douchen / Wassen")
    choice2 = input()
    if choice2.lower() == "douchen":
        print("Goedzo je bent iemand die goed om je hygiene geeft")
    elif choice2.lower() == "wassen":
        print("Laten we ons gaan wassen. het was beter geweest als je had gedouchet ")
    else:
        print(choice2, "is niet een geldig antwoord.")

time.sleep(1)
def dailychoices3():
    print("We moeten naar school toe wat ben je van plan om te doen? Met de trein of fietsen? Antwoord met: Trein / Fietsen")
    choice3 = input()
    if choice3.lower() == "trein":
        print("We gaan lekker met de trein ookal is dat wel lui.")
    elif choice3.lower() == "fietsen":
        print("We gaan lekker fietsen hartstikke gezond van je ga zo door!")
    else:
        print(choice3, "is niet een geldig antwoord.")

time.sleep(1)
def dailychoices4():
    print("Je komt op school aan en gaat naar binnen alles verloopt goed. Je komt aan in de pauze en krijgt opeens ruzie met iemand die je niet kent. Wat doe je? Sla je hem knock out of loop je weg? Antwoord met: Vechten / Weg Lopen")
    choice4 = input()
    if choice4.lower() == "vechten":
        print("Je slaat hem zo hard dat je hem KO slaat mooie rechter man maar nu heb je wel problemen.")
    elif choice4.lower() == "weg lopen":
        print("Goeie keuze dit soort mensen moet je geen aandacht geven.")
    else:
        print(choice4, "is niet een geldig antwoord.")

time.sleep(1)
def dailychoices5():
    print("We gaan weer naar huis toe, wat gaan we doen huiswerk of gamen? Antwoord met: Huiswerk / Gamen")
    choice5 = input()
    if choice5.lower() == "huiswerk":
        print("Lekker bezig maat! Je bent leer gierig.")
    elif choice5.lower() == "gamen":
        print("Is niet het beste wat je kan doen maar gamen is altijd leuk!")
    else:
        print(choice5, "is niet een geldig antwoord.")

dailychoices()
dailychoices2()
dailychoices3()
dailychoices4()
dailychoices5()
