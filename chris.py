products = [
    "pepperoni",
    "sausage",
    "green peppers",
    "red sauce",
    "white sauce",
    "thin crust",
    "thick crust"
]

def print_menu() -> None:
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
            print(f"Sorry, we don't have {ingredient}. Fool.")


if __name__ == "__main__":
    print_menu()
    create_pizza()