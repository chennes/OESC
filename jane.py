products = [
    "pepperoni",
    "sausage",
    "cheese",
    "green peppers",
    "white sauce",
    "red sauce",
    "thin crust"
]

def print_menu():
    for food in products:
        print(food)

def create_pizza() -> list[str]:
    print("Please create your pizza now:")
    ingredients = []
    while True:
        ingredient = input("Ingredient: ")
        if ingredient.lower() in products:
            ingredients.append(ingredient.lower())
        elif ingredient.lower() == "done":
            return ingredients
        else:
            print(f"Sorry, we don't have {ingredient}")


if __name__ == "__main__":
    print_menu()
    create_pizza()