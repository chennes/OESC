products = [
    "peperoni",
    "sausage",
    "green peppers",
    "red sauce",
    "white sauce",
    "thin crust",
    "thick crust"
]

def print_menu() -> None:
    """docstring goes here"""
    for food in products:
        print(food)

if __name__ == "__main__":
    print_menu()
