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

if __name__ == "__main__":
    print_menu()

