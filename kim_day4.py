inventory = {
    "apple" : 100,
    "banana" : 25,
    "orange" : 42,
    "grape" : 10000
}

for fruit_name,quantity in inventory.items():
    print(f"We have {quantity} {fruit_name}s")

#with open("fruit.txt", "w", encoding="utf-8") as f:   #opens file and calls f internally for writing
#    for fruit_name, quantity in inventory.items():
#        f.write(f"{fruit_name},{quantity}\n")

new_fruit_dict = {}                      #new dictionary
try:
    with open("fruit.txt", "r", encoding="utf-8") as f:   #opens file and calls f internally for reading
        contents = f.read()
    lines = contents.splitlines()
    for line in lines:                    #string of list 
        fruit_stuff = line.split(",") 
        if len(fruit_stuff) != 2:
            print("Invalid data")    
            continue
        fruit_name = fruit_stuff[0] #list of strings
        quantity = fruit_stuff[1]
        try:
            new_fruit_dict[fruit_name] = int(quantity)
        except ValueError:
            print(f"Invalid quantity for {fruit_name}: {quantity}")
            new_fruit_dict[fruit_name] = 0
except OSError as e:
    print("A bad thing happened:")
    print(e)
except ValueError as e:
    print("Conversion failed")
    print(e)
print(new_fruit_dict)