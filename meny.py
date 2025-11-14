from random import randint

def forts():
    input("Tryck [ENTER] för att fortsätta")
symbol = ["\u2780", "\u2781", "\u2782", "\u2783", "\u2784", "\u2785", "\u2786", "\u2787", "\u2788", "\u2789"]
bag = [""]
ätit = ["Det var gott", "Det var inte gott"]
mellanrum = 2
första = True
print("Välkommen till påsen")
while True:
    print("Visa inehållet [V]")
    print("Spara i påsen [S]")
    print("Ta bort från påsen [R]")
    print("Sök i påsen [F]")
    print("Ät ur påsen [E]")
    print("Avsluta programmet [Q]")
    for i in range(mellanrum):
        print("")
    choice = input("Vad vill du göra ")
    if choice.lower() == "v":
        for i in range(len(bag)):
            print(bag[i])
        forts()
    elif choice.lower() == "s" and len(bag) < 10:
        bag.append(input("Skriv vad du vill spara "))
        if första:
            bag.pop(0)
            första = False
    elif len(bag) == 10:
        print("Påsen är full")
        forts()
    elif choice.lower() == "r": 
        if första:
            print("Påsen är tom")
        else:
            for i in range(len(bag)):
                print(symbol[i], bag[i])
            rem = int(input("Skriv siffran till den du vill ta bort"))
            print(f"{bag[rem-1]} har tagits bort")
            bag.pop(rem-1)
        forts()
    elif choice.lower() == "f":
        query = input("vad vill du söka ")
        if query in bag:
            print(f"Hittade {query} i påsen")
        else:
            print(f"Hittade inte {query} i påsen")
        forts()
    elif choice.lower() == "e":
        meal = input("Skriv vad du vill äta ")
        if meal in bag:
            bag.remove(meal)
            print(ätit[randint(0, 1)])
        else:
            print(f"Det fanns inte {meal}")
        forts()
    elif choice.lower() == "q":
        break
    mellanrum = 3