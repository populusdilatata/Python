class Item:

  def __init__(self, name: str, price: float , quantity=0):

      # Run validation to the received arguments
      assert price >=0, f"Price {price} is not greater than zero!"
      assert quantity >=0, f"Quantity {quantity} is not greater than zero!"
      # Assign to self object
      self.name=name
      self.price=price
      self.quantity=quantity


  def calculate_total_price(self):
      return self.price*self.quantity

item1=Item("Phone", 100)

print(item1.name)
print(item1.price)
print(item1.quantity)

item2=Item("Laptop", -1000, -3 )
item2.has_numpad= False

print(item2.name)
print(item2.price)
print(item2.quantity)
