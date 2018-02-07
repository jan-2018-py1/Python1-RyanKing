class Product(object):
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, rate):
        return self.price * rate

    def return_item(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
            return self
        elif reason == "in box":
            self.status = "for sale"
            return self
        elif reason == "open box":
            self.status = "used"
            self.price *= 0.8
            return self

    def display_info(self):
        print "Price:", self.price
        print "Name:", self.name
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Status:", self.status
        return self

coffee = Product(5.00, "Coffee", "1lb", "Starbucks")
coffee.display_info()
coffee.add_tax(0.12)
coffee.return_item("open box").display_info()
