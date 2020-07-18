class IceCream:
    """IceCream class provides the function returning the cost of the ice-cream container"""
    def __init__(self, shape, flavour, quantity):
        self.shape = shape
        self.flavour = flavour
        self.quantity = quantity

    def shape_cost(self):
        if self.shape == "stick":
            return 5
        elif self.shape == "cup":
            return 10
        elif self.shape == "cone":
            return 20
        return 0


class Vanilla(IceCream):
    """Vanilla class provides the functions returning the flavour cost, total cost"""
    def __init__(self, shape, flavour, quantity):
        super().__init__(shape, flavour, quantity)

    def flavour_cost(self):
        return round(self.quantity / 100 * 30)

    def total_cost(self):
        return IceCream.shape_cost(self) + Vanilla.flavour_cost(self)


class Strawberry(IceCream):
    """Strawberry class provides the functions returning the flavour cost, total cost"""
    def __init__(self, shape, flavour, quantity):
        super().__init__(shape, flavour, quantity)

    def flavour_cost(self):
        return round(self.quantity / 100 * 35)

    def total_cost(self):
        return IceCream.shape_cost(self) + Strawberry.flavour_cost(self)


class Chocolate(IceCream):
    """Chocolate class provides the functions returning the flavour cost, topping cost, total cost"""
    def __init__(self, shape, flavour, quantity, topping):
        super().__init__(shape, flavour, quantity)
        self.topping = topping

    def flavour_cost(self):
        return round(self.quantity / 100 * 40)

    def topping_cost(self):
        if self.topping == "caramel":
            return 10
        elif self.topping == "nuts":
            return 10
        elif self.topping == "choco chip":
            return 15
        return 0

    def total_cost(self):
        return IceCream.shape_cost(self) + Chocolate.flavour_cost(self) + Chocolate.topping_cost(self)


print("Stick = Rs.5   Cup = Rs.10   Cone = Rs.20")
shape_var = input("Enter any of the shapes of the ice-cream given below\n(stick,   cup,   cone)\n")
print("We are providing ice-cream in grams")
quantity_var = int(input("Enter the quantity of the ice-cream like the example given below\nExample ( 120 )\n"))
print("Vanilla flavour 100g = Rs.30\nStrawberry flavour 100g = Rs.35\nChocolate flavour 100g = Rs.40")
flavour_var = input("Enter any of the flavours of the ice-cream given below\n(vanilla,   strawberry,   chocolate)\n")
if flavour_var == "chocolate":
    print("Chocolate ice-cream has various toppings")
    print("Caramel topping cost = Rs.10\nNuts topping cost = Rs.10\nChoco-chip topping cost = Rs.15")
    topping_var = input("Enter any of the toppings of the ice-cream given below\n(caramel,   nuts,   choco chip)\n")
    # Object instantiation
    ice_cream_obj = Chocolate(shape_var, flavour_var, quantity_var, topping_var)
elif flavour_var == "vanilla":
    # Object instantiation
    ice_cream_obj = Vanilla(shape_var, flavour_var, quantity_var)
elif flavour_var == "strawberry":
    # Object instantiation
    ice_cream_obj = Strawberry(shape_var, flavour_var, quantity_var)
print("The total cost of the ice-cream is {}".format(ice_cream_obj.total_cost()))
'''
Output1:
Stick = Rs.5   Cup = Rs.10   Cone = Rs.20
Enter any of the shapes of the ice-cream given below
(stick,   cup,   cone)
cone
We are providing ice-cream in grams
Enter the quantity of the ice-cream like the example given below
Example ( 120 )
500
Vanilla flavour 100g = Rs.30
Strawberry flavour 100g = Rs.35
Chocolate flavour 100g = Rs.40
Enter any of the flavours of the ice-cream given below
(vanilla,   strawberry,   chocolate)
chocolate
Chocolate ice-cream has various toppings
Caramel topping cost = Rs.10
Nuts topping cost = Rs.10
Choco-chip topping cost = Rs.15
Enter any of the toppings of the ice-cream given below
(caramel,   nuts,   choco chip)
choco chip
The total cost of the ice-cream is 235


Output2:
Stick = Rs.5   Cup = Rs.10   Cone = Rs.20
Enter any of the shapes of the ice-cream given below
(stick,   cup,   cone)
cup
We are providing ice-cream in grams
Enter the quantity of the ice-cream like the example given below
Example ( 120 )
1000
Vanilla flavour 100g = Rs.30
Strawberry flavour 100g = Rs.35
Chocolate flavour 100g = Rs.40
Enter any of the flavours of the ice-cream given below
(vanilla,   strawberry,   chocolate)
vanilla
The total cost of the ice-cream is 310


Output3:
Stick = Rs.5   Cup = Rs.10   Cone = Rs.20
Enter any of the shapes of the ice-cream given below
(stick,   cup,   cone)
stick
We are providing ice-cream in grams
Enter the quantity of the ice-cream like the example given below
Example ( 120 )
100
Vanilla flavour 100g = Rs.30
Strawberry flavour 100g = Rs.35
Chocolate flavour 100g = Rs.40
Enter any of the flavours of the ice-cream given below
(vanilla,   strawberry,   chocolate)
strawberry
The total cost of the ice-cream is 40
'''