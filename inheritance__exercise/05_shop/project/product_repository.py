from typing import List

from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for p in self.products:
            if p.name == product_name:
                return p

    def remove(self, product_name: str):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):

        return "\n".join([f"{x.name}: {x.quantity}" for x in self.products])

