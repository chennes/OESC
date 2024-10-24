#Python Pixxa Deliveries

def print_menu():
    for items in products:
        print(items)
        
products = ["pepperoni", "sausage", "green peppers", "red sauce", "white sauce", "thin crust", "thick crust"]

if __name__ == "__main__":
    print_menu()

pizzaSize = input("What size pizza would you like? S, M, L: ")
pizzaSize = pizzaSize.upper()
addPepperoni = input("Would you like pepperoni on your pizza? Y or N: ")
addPepperoni = addPepperoni.upper()
addExtraCheese = input("Would you like to add extra cheese? Y or N: ")
addExtraCheese = addExtraCheese.upper()
orderTotal = 0

# todo: work out how much the need to pay based on the size choice 
if pizzaSize == 'L':
    orderTotal += 25
elif pizzaSize == 'M':
    orderTotal += 20
elif pizzaSize == 'S':
    orderTotal += 15
else:
    print("Not a valid pizza size")

# todo: work out how much to add to their total if they want to add pepperoni

if addPepperoni == 'Y':
    if pizzaSize == 'S':
        orderTotal += 2
    else:
        orderTotal += 3

# todo: work out how much to add to their total if they want extra cheese

if addExtraCheese == 'Y':
    orderTotal += 1

print(f"Your total is going to be ${orderTotal}")

