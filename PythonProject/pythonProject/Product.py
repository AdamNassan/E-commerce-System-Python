from datetime import datetime
class Product:
    def __init__(self, product_id, product_name, product_category, price, inventory,supplier, has_an_offer, offer_price, valid_until):
        self.product_id = product_id
        self.product_name = product_name
        self.product_category = product_category
        self.price = price
        self.inventory = inventory
        self.supplier = supplier
        self.has_an_offer = bool(int(has_an_offer))
        self.offer_price = offer_price
        self.valid_until = valid_until
