from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):
    def setUp(self):
        self.shoppingcart = ShoppingCart("ShopName", 1000)
        self.shoppingcart2 = ShoppingCart("ShopNameTwo", 2000)
        self.shoppingcart.products = {}
        self.shoppingcart2.products = {"Mouse": 300.00, "Webcam": 500.00}

    def test_if_initialization_is_correct(self):
        self.assertEqual("ShopName", self.shoppingcart.shop_name)
        self.assertEqual(1000, self.shoppingcart.budget)
        self.assertEqual({}, self.shoppingcart.products)

    def test_if_shop_name_setter_raises_value_err(self):
        with self.assertRaises(ValueError) as ve:
            self.shoppingcart.shop_name = "9s"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_if_shopname_setter_works_correctly(self):
        self.shoppingcart.shop_name = "MaonStore"
        self.assertEqual("MaonStore", self.shoppingcart.shop_name)

    def test_if_adding_to_cart_too_expensive_product_raises_value_err(self):
        with self.assertRaises(ValueError) as ve:
            self.shoppingcart.add_to_cart("Product", 101)
        self.assertEqual("Product Product cost too much!", str(ve.exception))

    def test_when_successfully_add_product_returns_correct_msg(self):
        result = self.shoppingcart.add_to_cart("Joystick", 99.99)
        self.assertEqual({"Joystick": 99.99}, self.shoppingcart.products)
        self.assertEqual("Joystick product was successfully added to the cart!", result)

    def test_if_removing_not_existed_product_from_cart_raises_value_err(self):
        with self.assertRaises(ValueError) as ve:
            self.shoppingcart.products = {"Joystick": 99.99}
            self.shoppingcart.remove_from_cart("Keyboard")
        self.assertEqual("No product with name Keyboard in the cart!", str(ve.exception))

    def test_if_removing_product_from_cart_returns_correct_msg(self):
        self.shoppingcart.products = {"Joystick": 99.99}
        result = self.shoppingcart.remove_from_cart("Joystick")
        self.assertEqual({}, self.shoppingcart.products)
        self.assertEqual("Product Joystick was successfully removed from the cart!", result)

    def test_when_not_having_enough_budget_raises_value_ERR(self):
        with self.assertRaises(ValueError) as ve:
            self.shoppingcart.products = {"Joystick": 100.00, "Joystick2": 901.00}
            self.shoppingcart.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 1.00lv!", str(ve.exception))

    def test_if_adding_concats_returns_correct_msg(self):
        first = ShoppingCart('Test', 200)
        first.add_to_cart('from_first', 1)
        second = ShoppingCart('SecondTest', 100)
        second.add_to_cart('from_second', 2)
        merged = first.__add__(second)
        self.assertEqual('TestSecondTest', merged.shop_name)
        self.assertEqual(300, merged.budget)
        self.assertEqual({'from_first': 1, 'from_second': 2}, merged.products)

    def test_when_buing_products_returns_correct_msg(self):
        self.shoppingcart.products = {"Joystick": 100.00, "Joystick2": 899.00}
        result = self.shoppingcart.buy_products()
        self.assertEqual("Products were successfully bought! Total cost: 999.00lv.", result)


if __name__ == "__main__":
    main()
