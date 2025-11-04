run = True
print("Välkommen till påsen")
bag = []
while run:
    print("Visa inehållet [V]")
    print("Spara i påsen [S]")
    print("")
    print("Avsluta programmet [Q]")
    choice = input("Vad vill du göra ")
    if choice.lower() == "v":
        print(bag)
    elif choice.lower() == "s":
        bag.append(input("Skriv vad du vill spara "))
    elif choice.lower() == "q":
        run = False