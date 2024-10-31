inventory = {    #dictionary is defined by curly braces
    "apple" : 100,
    "banana" : 25,
    "orange" : 42,
    "grape" : 10000
}

for fruit_name,quantity in inventory.items(): #unpacks the dictionary into 2 fields
    print(f"We have {quantity} {fruit_name}s")

with open("fruit.txt", "w", encoding="utf-8") as f:  #opens a disk file, alllows writes calling it f locally
    for fruit_name, quantity in inventory.items():   #writes a file - \n force new line
        f.write(f"{fruit_name},{quantity}\n")

try:
    with open("fruits.txt", "r", encoding="utf-8") as f:
        pass
except OSError as e:                         #coding for errors
    print("A bad thing happened:")
    print(e)