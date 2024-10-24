products = [
    "pepperoni",
    "sauage",
    "green peppers",
    "red sauce",
    "white sauce",
    "thin crust",
    "thick Crust"
]

def print_menu() -> None:
    for food in products:
        print(food)

def create_pizza() -> list[str]:
    print ("Please create your pizza now:")
    ingredients = []
    while True:
        ingredient = input("ingredient: ")
        if ingredient.lower() in products:
            ingredients.append(ingredient.lower)
        elif ingredient.lower() == "done":
            return ingredients
        else:
            print(f"Sorry, we don't have that {ingredient}")


if __name__ == "__main__":
    print_menu()
    create_pizza()

