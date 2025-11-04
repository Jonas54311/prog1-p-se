bag = []
print("Välkommen till påsen")
while True:
    print("Visa inehållet [V]")
    print("Spara i påsen [S]")
    print("Ta bort från påsen [R]")
    print("Avsluta programmet [Q]")
    choice = input("Vad vill du göra ")
    if choice.lower() == "v":
        for i in range(len(bag)):
            print(bag[l])
        input("Tryck [ENTER] för att fortsätta")
    elif choice.lower() == "s" and len(bag) < 10:
        bag.append(input("Skriv vad du vill spara "))
    elif len(bag) == 10:
        print("Påsen är full")
    elif choice.lower() == "r":
        bag.remove(input("Skriv vad du vill ta bort"))
    elif choice.lower() == "q":
        break
    for i in range(5):
        print("")