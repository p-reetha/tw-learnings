class Shopkeeper:
    tax_list = []

    def __init__(self, id_str, name, price, category):
        self.id_str = id_str
        self.name = name
        self.price = price
        self.category = category
        self.tax = 0
        self.price_after_tax = 0
        # normal tax
        if self.price >= 500:
            self.tax = 0.05
        else:
            self.tax = 0.02
        # special tax
        if self.category == "textile":
            self.tax = self.tax + 0.01
        elif self.category == "dairy" and self.price >= 1000:
            self.tax = self.tax + 0.03
        Shopkeeper.tax_list.append("%.2f" % self.tax)

    def apply_tax(self):
        self.price_after_tax = self.price * (1 + self.tax)
        return "%2.f" % self.price_after_tax


prod1 = Shopkeeper("09977", "apple", 250, "produce")
prod2 = Shopkeeper("6757687", "ghee", 400, "dairy")
prod3 = Shopkeeper("435657", "jeans", 1150, "textile")
prod4 = Shopkeeper("0825", "leggings", 300, "textile")
prod5 = Shopkeeper("0826", "leggings", 350, "textile")
prod6 = Shopkeeper("09800", "onion", 500, "produce")
prod7 = Shopkeeper("2409", "soap", 100, "home needs")
prod8 = Shopkeeper("8786", "utensil", 700, "home needs")
prod9 = Shopkeeper("455675", "ice-cream", 1001, "dairy")


print("In the following list, taxes are appear in the same order as their objects are instantiated")
print(Shopkeeper.tax_list)
print(Shopkeeper.apply_tax(prod1))
print(Shopkeeper.apply_tax(prod2))
print(Shopkeeper.apply_tax(prod3))
print(Shopkeeper.apply_tax(prod4))
print(Shopkeeper.apply_tax(prod5))
print(Shopkeeper.apply_tax(prod6))
print(Shopkeeper.apply_tax(prod7))
print(Shopkeeper.apply_tax(prod8))
print(Shopkeeper.apply_tax(prod9))