class Catalogue:
    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, product_name):
        Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter):
        return [x for x in Catalogue.products if x[0] == first_letter]

    def __repr__(self):
        res = f"Items in the {self.name} catalogue:\n"
        res += "\n".join(sorted(Catalogue.products))
        return res


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
