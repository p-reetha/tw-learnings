class IceCream:
    """IceCream class provides the functions returning the shape cost, flavour cost, topping cost, total cost"""
    def __init__(self, shape, flavour, quantity, topping=None):
        self.shape = shape
        self.flavour = flavour
        self.quantity = quantity
        self.topping = topping
    def shape_cost(self):
        if self.shape == "stick":
            return 5
        elif self.shape == "cup":
            return 10
        elif self.shape == "cone":
            return 20
    def flavour_cost(self):
        if self.flavour == "vanilla":
            return round(self.quantity * 0.3)
        elif self.flavour == "strawberry":
            return round(self.quantity * 0.35)
        elif self.flavour == "chocolate":
            return round(self.quantity * 0.4)
    def topping_cost(self):
        if self.topping == "caramel":
            return 10
        elif self.topping == "nuts":
            return 10
        elif self.topping == "choco chip":
            return 15
        return 0
    def total_cost(self):
        return self.shape_cost() + self.flavour_cost() + self.topping_cost()


shape_var = input("Stick = Rs.5   Cup = Rs.10   Cone = Rs.20\nEnter any of the shapes of the ice-cream given below\n(stick,   cup,   cone)\n")
flavour_var = input("Vanilla flavour 100g = Rs.30\nStrawberry flavour 100g = Rs.35\nChocolate flavour 100g = Rs.40\nEnter any of the flavours of the ice-cream given below\n(vanilla,   strawberry,   chocolate)\n")
quantity_var = int(input("Enter the quantity of the ice-cream like the example given below\nExample ( 120 )\n"))
topping_var = ""
if flavour_var == "chocolate":
    topping_var = input("Chocolate ice-cream has various toppings\nCaramel topping cost = Rs.10\nNuts topping cost = Rs.10\nChoco-chip topping cost = Rs.15\nEnter any of the toppings of the ice-cream given below\n(caramel,   nuts,   choco chip)\n")
ice_cream_obj = IceCream(shape_var, flavour_var, quantity_var, topping_var)
print("\nThe total cost of the ice-cream is {}".format(ice_cream_obj.total_cost()))
'''
Sample Output:
Stick = Rs.5   Cup = Rs.10   Cone = Rs.20
Enter any of the shapes of the ice-cream given below
(stick,   cup,   cone)
cone
Vanilla flavour 100g = Rs.30
Strawberry flavour 100g = Rs.35
Chocolate flavour 100g = Rs.40
Enter any of the flavours of the ice-cream given below
(vanilla,   strawberry,   chocolate)
chocolate
Enter the quantity of the ice-cream like the example given below
Example ( 120 )
500
Chocolate ice-cream has various toppings
Caramel topping cost = Rs.10
Nuts topping cost = Rs.10
Choco-chip topping cost = Rs.15
Enter any of the toppings of the ice-cream given below
(caramel,   nuts,   choco chip)
choco chip

The total cost of the ice-cream is 235
'''