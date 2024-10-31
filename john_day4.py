#john_day4

inventory = {
    "apple":100,
    "banana":25,
    "orange":42,
    "grapes":10000
}

# for fruit in inventory:
#     print(fruit)

f = open("john_day4.txt", "w", encoding ='utf-8')
f.write("Store inventory list\n\n")
f.close()
f = open("john_day4.txt", "a", encoding ='utf-8')
for k, v in inventory.items():
    f.write(str(k) + ": " + str(v) + "\n")
f.close()

try:
    with open("john_day3.txt", "r", encoding = 'utf-8') as f:
        contents = f.read()
        print(contents)
except OSError as e:
    print(f"{e}")
finally:
    exit()
