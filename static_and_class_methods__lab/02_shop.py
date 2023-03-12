from typing import Dict


class Shop:

    def __init__(self, name: str, shop_type: str, capacity: int):
        self.name = name
        self.type = shop_type
        self.capacity = capacity
        self.items: Dict[str: int] = {}

    @classmethod
    def small_shop(cls, name: str, shop_type: str):
        CAPACITY = 10
        return cls(name, shop_type, CAPACITY)

    def add_item(self, item_name: str):
        if item_name not in self.items.keys():
            self.items[item_name] = 0

        if sum(values for values in self.items.values()) < self.capacity:
            self.items[item_name] += 1

            return f"{item_name} added to the shop"

        return "Not enough capacity in the shop"

    def remove_item(self, item_name: str, amount: int):
        if item_name in self.items.keys():

            if self.items[item_name] - amount >= 0:
                self.items[item_name] -= amount

                if not self.items[item_name]:
                    del self.items[item_name]
                return f"{amount} {item_name} removed from the shop"

        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)
