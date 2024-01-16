class Cart:
    #class attributes
    flat_discount=0
    min_bill=100
    #instance attributes
    def __init__(self):
        self.items={}
    def add_item(self, iten_name, quantity):
        self.items[iten_name]=quantity
    def display_items(self):
        print(self.items)
    def print_min_bill(self):
        print(Cart.min_bill)
    @classmethod
    def update_flat_discount(cls, new_flat_discount):
        cls.flat_discount=new_flat_discount
    
    @classmethod
    def increase_flat_discount(cls, amount):
        new_flat_discount = cls.flat_discount + amount
        cls.update_flat_discount(new_flat_discount)
    
a=Cart()
a.add_item("book", 3)
a.add_item("lap", 4)
a.display_items()
print(Cart.min_bill)

a=Cart()
b=Cart()
Cart.min_bill=200
print(a.print_min_bill())
print(b.print_min_bill())

# Cart.update_flat_discount(25)
# print(Cart.flat_discount)ḥ

Cart.increase_flat_discount(50)
print(Cart.flat_discount)

