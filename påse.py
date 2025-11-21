from random import randint

def forts():
    input("Tryck [ENTER] för att fortsätta")
symbol = ["\u2780", "\u2781", "\u2782", "\u2783", "\u2784", "\u2785", "\u2786", "\u2787", "\u2788", "\u2789"]
bag = ["Påsen är tom"]
ätit = ["Det var gott", "Det var inte gott"]
print("           .¨.")
print("            ¨ ")
print(":::::.    .:::.   .::'::.  :::::::  ::.  ::")
print("::   ::  .:: ::.  ::.  ''  ::       :::. ::")
print(":::::'   ::...::   ':::.   :::::    ::':.::")
print("::       ::'''::  ..  '::  ::       :: ':::")
print("::       ::   ::  '::.::'  :::::::  ::  '::")
print(" \n")
forts()
while True:
    print("Visa inehållet     [V]")
    print("Spara i påsen      [S]")
    print("Ta bort från påsen [R]")
    print("Sök i påsen        [F]")
    print("Ät ur påsen        [E]")
    print("Töm påsen          [T]")
    print("Spräng påsen       [B]")
    print("Avsluta programmet [Q]")
    print("")
    choice = input("Vad vill du göra ")
    if choice.lower() == "v":
        for i in range(len(bag)):
            print(bag[i])
        forts()
    elif choice.lower() == "s" and len(bag) < 10:
        bag.append(input("Skriv vad du vill spara "))
        if bag[0] == "Påsen är tom":
            bag.pop(0)
    elif len(bag) == 10:
        print("Påsen är full")
        forts()
    elif choice.lower() == "r" and bag[0] == "Påsen är tom":
        print(bag[0])
    elif choice.lower() == "r" and bag[0] != "påsen är tom": 
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
    elif choice.lower() == "t":
        bag = ["Påsen är tom"]
        print("Påsen är nu tom")
        forts()
    elif choice.lower() == "b":
        print("   *.''''.   ..")
        print("  *:      '.:::::.")
        print(" * :     .:::::::::.")
        print("  *    ':::::::::::::.")
        print("  (       ':::::::::::::.")
        print(" (*)        ':::::::::::::.")
        print(" :             ':::::::::::::.")
        print(":                 ':::::::::::::.")
        boom = input("Är du säker på att du vill spränga påsen? (y/n) ")
        if boom.lower() == "y":
            print("::::::::.        .:::.         .:::.      :::        :::   ::")
            print("::     '::.    .::' '::.     .::' '::.    :::.      .:::   ::")
            print("::       ::   .:'     ':.   .:'     ':.   ::::      ::::   ::")
            print("::    .:::'   ::       ::   ::       ::   :: ::    :: ::   ::")
            print(":::::::::     ::       ::   ::       ::   :: ':.  .:' ::   ::")
            print("::    ':::.   ::       ::   ::       ::   ::  ::  ::  ::   ::")
            print("::       ::   ':.     .:'   ':.     .:'   ::   ::::   ::   ")
            print("::     .::'    '::. .::'     '::. .::'    ::   '::'   ::   ::")
            print("::::::::         ':::'         ':::'      ::    ::    ::   ::")
            break
        else:
            print("påsen sprängdes inte")
            forts()
    elif choice.lower() == "q":
        break