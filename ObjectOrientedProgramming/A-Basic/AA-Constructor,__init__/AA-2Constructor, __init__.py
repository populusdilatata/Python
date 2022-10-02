class Item:

  def __init__(self, name, price, quantity=0):
      print(f"An instance created: {name}")
      self.name=name
      self.price=price
      self.quantity=quantity

  def calculate_total_price(self):
      return self.price*self.quantity

item1=Item("Phone", 100)

print(item1.name)
print(item1.price)
print(item1.quantity)

item2=Item("Laptop", 1000, 3 )
item2.has_numpad= False

print(item2.name)
print(item2.price)
print(item2.quantity)
