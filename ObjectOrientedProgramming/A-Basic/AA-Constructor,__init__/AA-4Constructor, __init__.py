class Item:
    pay_rate =0.8 # The pay rate after 20% discount
    def __init__(self, name: str, price: float , quantity=0):


      # Run validation to the received arguments
      assert price >=0, f"Price {price} is not greater than zero!"
      assert quantity >=0, f"Quantity {quantity} is not greater than zero!"
      # Assign to self object
      self.name=name
      self.price=price
      self.quantity=quantity

    def apply_discount(self):
              self.price = self.price*self.pay_rate
    def calculate_total_price(self):
        return self.price*self.quantity








item1=Item("Phone", 100)
item1.apply_discount()
print(item1.price)

item2=Item("Laptop", 1000, 3 )
item2.pay_rate=0.7
item2.apply_discount()
print(item2.price)
#print(Item.__dict__) # All the attributes for Class level
#print(item1.__dict__) # All the attributes for instance level
