from crust import Crust
from sauce import Sauce
from typing import Optional

class PizzaError(RuntimeError):
    """Error class for pizza problems"""

class Pizza:

    def __init__(self, crust_style:Crust):
        """Create a pizza with a given crust. Options
        for crust style are thin, thick, and pan."""
        if not isinstance(crust_style, Crust):
            raise PizzaError("You are a terrible programmer.")
        self.crust = crust_style
        self.sauce = None
        self.toppings = []

    def __str__(self):
        result = f"Pizza: {self.crust} crust pizza\n"
        result += f"  Sauce: {self.sauce}\n"
        if self.toppings:
            result += "  Toppings:\n"
            for topping in self.toppings:
                result += f"    {topping}\n"
        return result


    def set_sauce(self, requested_sauce:Optional[Sauce]):
        if not isinstance(requested_sauce, Sauce) and \
            requested_sauce is not None:
            raise PizzaError(f"Not a sauce")
        self.sauce = requested_sauce

    def add_topping(self, topping:str):
        available_toppings = ["cheese", "pepperoni", "mushrooms", "anchovies"]
        if topping not in available_toppings:
            raise PizzaError(f"Topping {topping} not available")
        if len(self.toppings) >= 4:
            raise PizzaError("Too many toppings")
        self.toppings.append(topping)

    def remove_topping(self, topping:str):
        try:
            self.toppings.remove(topping)
        except ValueError:
            pass

    def clear_toppings(self):
        self.toppings.clear()

    def bake(self):
        print(f"Now baking: {self}")