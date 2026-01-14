foods = []
while True:
    f = input("What food do you like?: ")
    if f == "quit":
        break
    foods.append(f)
    
#walrus operator    
foods = []
while (f := input("What food do you like? (type 'quit' to stop): ")) != "quit":
    foods.append(f)    