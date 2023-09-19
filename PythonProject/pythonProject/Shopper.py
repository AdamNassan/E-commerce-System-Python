from Admin import Admin
class Shopper(Admin):
    def __init__(self, user_id, user_name, user_date_of_birth, role, active, basket, order):
        super().__init__(user_id, user_name, user_date_of_birth, role, active)
        self.basket = {}
        self.add_to_basket(basket)
        self.order = int(order)

    def add_to_basket(self, basket_str):
        if basket_str:
            items = basket_str.strip('{}').split(',')
            if items != ['']:
                for item in items:
                    product_id, quantity = item.split(':')
                    self.basket[product_id] = int(quantity)



    def place_order(self):
        if self.basket:
            self.order = 1
            print("Order placed successfully.")
        else:
            print("Your basket is empty. Please add items to your basket before placing an order.")