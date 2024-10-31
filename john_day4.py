#john_day4

inventory = {
    "apple":100,
    "banana":25,
    "orange":42,
    "grapes":10000
}

# for fruit in inventory:
#     print(fruit)

print("Store inventory list")
for k, v in inventory.items():
    print(f"{k}: {v}")
    
