class Product:
    def __init__(self, id_str, name, price, category):
        self.id_str = id_str
        self.name = name
        self.price = price
        self.category = category
        self.nrml_tax = 0

    def normal_tax(self):
        if self.price >= 500:
            self.nrml_tax = self.price * (5 / 100)
        else:
            self.nrml_tax = self.price * (2 / 100)
        return self.nrml_tax


class Textile(Product):
    def __init__(self, id_str, name, price, category):
        super().__init__(id_str, name, price, category)
        self.textl_tax = 0

    def textile_tax(self):
        self.textl_tax = Product.normal_tax(self) + self.price * (1 / 100)
        return self.textl_tax


class Dairy(Product):
    def __init__(self, id_str, name, price, category):
        super().__init__(id_str, name, price, category)
        self.dair_tax = 0

    def dairy_tax(self):
        if self.price > 1000:
            self.dair_tax = self.price * (3 / 100)
        return round(self.dair_tax)


prod1 = Product("09977", "apple", 250, "produce")
prod2 = Dairy("6757687", "ghee", 400, "dairy")
prod3 = Textile("435657", "jeans", 1150, "textile")
prod4 = Textile("0825", "leggings", 300, "textile")
prod5 = Textile("0826", "leggings", 350, "textile")
prod6 = Product("09800", "onion", 500, "produce")
prod7 = Product("2409", "soap", 100, "home needs")
prod8 = Product("8786", "utensil", 700, "home needs")
prod9 = Dairy("455675", "ice-cream", 1001, "dairy")
print("Tax for {0} is: {1}".format(prod1.name, prod1.normal_tax()))
print("Tax for {0} is: {1}".format(prod2.name, prod2.dairy_tax()))
print("Tax for {0} is: {1}".format(prod3.name, prod3.textile_tax()))
print("Tax for {0} is: {1}".format(prod4.name, prod4.textile_tax()))
print("Tax for {0} is: {1}".format(prod5.name, prod5.textile_tax()))
print("Tax for {0} is: {1}".format(prod6.name, prod6.normal_tax()))
print("Tax for {0} is: {1}".format(prod7.name, prod7.normal_tax()))
print("Tax for {0} is: {1}".format(prod8.name, prod8.normal_tax()))
print("Tax for {0} is: {1}".format(prod9.name, prod9.dairy_tax()))

'''
Output:
Tax for apple is: 5.0
Tax for ghee is: 0
Tax for jeans is: 69.0
Tax for leggings is: 9.0
Tax for leggings is: 10.5
Tax for onion is: 25.0
Tax for soap is: 2.0
Tax for utensil is: 35.0
Tax for ice-cream is: 30
'''