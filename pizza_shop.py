from pizza import Pizza, PizzaError
from crust import Crust
from sauce import Sauce

try:
    first_pizza = Pizza(Crust.THIN)
    second_pizza = Pizza(Crust.PAN)
except PizzaError as e:
    print(e)

if __name__ == "__main__":
    first_pizza.set_sauce(Sauce.PESTO)
    first_pizza.add_topping("cheese")
    first_pizza.add_topping("mushrooms")
    first_pizza.bake()
