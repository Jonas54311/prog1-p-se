from random import randint

def contin():
    input("Tryck [ENTER] för att fortsätta")
bag = [""]
ätit = ["Det var gott", "Det var inte gott"]
mellanrum = 2
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
        contin()
    elif choice.lower() == "s" and len(bag) < 10:
        bag.append(input("Skriv vad du vill spara "))
    elif len(bag) == 10:
        print("Påsen är full")
        contin()
    elif choice.lower() == "r":
        bag.remove(input("Skriv vad du vill ta bort "))
    elif choice.lower() == "f":
        query = input("vad vill du söka ")
        if query in bag:
            print(f"Hittade {query} i påsen")
        else:
            print(f"Hittade inte {query} i påsen")
        contin()
    elif choice.lower() == "e":
        meal = input("Skriv vad du vill äta ")
        if meal in bag:
            bag.remove(meal)
            print(ätit[randint(0, 1)])
        else:
            print(f"Det fanns inte {meal}")
        contin()
    elif choice.lower() == "q":
        break
    mellanrum = 3