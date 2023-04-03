from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    VALID_MEALS = {
        "Starter": Starter,
        "MainDish": MainDish,
        "Dessert": Dessert,
    }
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        if client_phone_number in [c.phone_number for c in self.clients_list]:
            raise Exception("The client has already been registered!")
        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ not in FoodOrdersApp.VALID_MEALS.keys():
                continue
            self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return "\n".join([meal.details() for meal in self.menu])

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        if client_phone_number not in [c.phone_number for c in self.clients_list]:
            self.clients_list.append(Client(client_phone_number))

        meal_not_in_menu = [meal for meal in meal_names_and_quantities.keys() if
                            meal not in [m.name for m in self.menu]]
        if meal_not_in_menu:
            raise Exception(f"{meal_not_in_menu[0]} is not on the menu!")

        current_menu_dict = {}
        for meal in self.menu:
            current_menu_dict[meal.name] = meal.quantity
        qty_is_not_enough = {k: v for (k, v) in meal_names_and_quantities.items() if v > current_menu_dict[k]}
        if qty_is_not_enough:
            meal_type = [meal.__class__.__name__ for meal in self.menu if meal.name in qty_is_not_enough.keys()][0]
            meal_name = [meal.name for meal in self.menu if meal.name in qty_is_not_enough.keys()][0]
            raise Exception(f"Not enough quantity of {meal_type}: {meal_name}!")

        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        for meal in meal_names_and_quantities.items():
            meal_name = meal[0]
            meal_qty = meal[1]
            meal_price = [m.price for m in self.menu if m.name == meal_name][0]
            meal_obj_to_add = next(filter(lambda m: m.name == meal_name, self.menu))
            client.shopping_cart.append(meal_obj_to_add)
            client.bill += meal_price * meal_qty
            meal_obj_to_add.quantity -= meal_qty

        return f"Client {client_phone_number} successfully ordered {', '.join([m.name for m in client.shopping_cart])} for {client.bill:.2f}lv."

    def no_meals_in_shopping_card(self, client_obj):
        if not client_obj.shopping_cart:
            raise Exception("There are no ordered meals!")

    def reset_client_card_and_bill(self, client_obj):
        client_obj.shopping_cart = []
        client_obj.bill = 0

    def cancel_order(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        self.no_meals_in_shopping_card(client)

        for meal in client.shopping_cart:
            meal_name = meal.name
            meal_qty = meal.quantity
            meal_obj_to_restore_qty = next(filter(lambda m: m.name == meal_name, self.menu))
            meal_obj_to_restore_qty.quantity += meal_qty
        self.reset_client_card_and_bill(client)

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):

        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        client_bill_amount = client.bill
        self.no_meals_in_shopping_card(client)
        self.reset_client_card_and_bill(client)

        FoodOrdersApp.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {client_bill_amount:.2f} was successfully paid for {client_phone_number}."

    def __str__(self, ):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."


food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
print(food_orders_app.register_client("0899999998"))
french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
print(food_orders_app.add_meals_to_menu(
    french_toast, hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets))
print(food_orders_app.show_menu())
food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
additional_food = {"Risotto with Wild Mushrooms": 2,
                   "Tortilla with Beef and Pork": 2}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
print(food_orders_app.add_meals_to_shopping_cart('0899999998', **{"Risotto with Wild Mushrooms": 2,
                                                                "Tortilla with Beef and Pork": 2}))
print(food_orders_app.cancel_order("0899999998"))
print(food_orders_app.cancel_order("0899999998"))
print(food_orders_app.finish_order("0899999999"))
print(food_orders_app)
