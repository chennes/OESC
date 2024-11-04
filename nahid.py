products = [
    "pepproni",
    "sausage",
    "green peppers",
    "red sauce",
    "white sauce",
    "thin crust",
    "thick crust" 
]
#write a function that prints out the ingedients in the list above

def print_menu() -> None:
    for food in products:
        print(food)
#returns a list of strings
def create_pizza() -> list[str]:
    print("Please create your pizza now:")
# need a loop that would requir a done to end  while loop . ingredients is a storage location we need    
    ingredients = []
    while True:
        ingredient = input("Ingredient: ")
        if ingredient.lower() in products:
            ingredients.append(ingredient.lower())
        elif ingredient.lower() == "done":
            return ingredients
        else:
            print(f"Sorry, we dont have {ingredient}")  

  

if __name__ == "__main__":
    print_menu() 
    create_pizza()
          
