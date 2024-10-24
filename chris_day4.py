inventory = {
    "apple" : 100,
    "banana" : 25,
    "orange" : 42,
    "grape" : 10000
}

for fruit_name,quantity in inventory.items():
    print(f"We have {quantity} {fruit_name}s")

with open("fruit.txt", "w", encoding="utf-8") as f:
    for fruit_name, quantity in inventory.items():
        f.write(f"{fruit_name},{quantity}\n")

try:
    with open("fruits.txt", "r", encoding="utf-8") as f:
        pass
except OSError as e:
    print("A bad thing happened:")
    print(e)