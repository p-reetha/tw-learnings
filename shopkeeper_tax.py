class Shopkeeper:

    def __init__(self, id_str, name, price, category):
        self.id_str = id_str
        self.name = name
        self.price = price
        self.category = category
        self.tax = 0

    def normal_tax(self):
        if self.price >= 500:
            self.tax = 5
        else:
            self.tax = 2
        return self.tax


class SpecialTax(Shopkeeper):

    def __init__(self, id_str, name, price, category):
        self.spl_tax = 0
        Shopkeeper.__init__(self, id_str, name, price, category)

    def special_tax(self):
        if self.category == "textile":
            self.spl_tax = 1
        elif self.category == "dairy" and self.price >= 1000:
            self.spl_tax = 3
        return self.spl_tax


def total_tax(*products):
    tax_list = []
    price_list_after_tax = []
    for product in products:
        final_tax = product.normal_tax() + product.special_tax()
        tax_list.append(final_tax)
        prod_price_after_tax = int(product.price * (1 + final_tax / 100))
        price_list_after_tax.append(prod_price_after_tax)
    print("Taxes for each products in percentage ", tax_list)
    print("Prices of products after applying tax ", price_list_after_tax)


prod1 = SpecialTax("09977", "apple", 250, "produce")
prod2 = SpecialTax("6757687", "ghee", 400, "dairy")
prod3 = SpecialTax("435657", "jeans", 1150, "textile")
prod4 = SpecialTax("0825", "leggings", 300, "textile")
prod5 = SpecialTax("0826", "leggings", 350, "textile")
prod6 = SpecialTax("09800", "onion", 500, "produce")
prod7 = SpecialTax("2409", "soap", 100, "home needs")
prod8 = SpecialTax("8786", "utensil", 700, "home needs")
prod9 = SpecialTax("455675", "ice-cream", 1001, "dairy")
print("In the following list, taxes appear in the same order as their objects are instantiated")
total_tax(prod1, prod2, prod3, prod4, prod5, prod6, prod7, prod8, prod9)
'''
Output:
In the following list, taxes appear in the same order as their objects are instantiated
Taxes for each products in percentage  [2, 2, 6, 3, 3, 5, 2, 5, 8]
Prices of products after applying tax  [255, 408, 1219, 309, 360, 525, 102, 735, 1081]
'''