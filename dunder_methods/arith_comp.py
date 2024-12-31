class InventoryItem:
    """Class to demonstrate the operator overloading for inventory management."""
    def __init__(self, name, quantity):
        self.name = name 
        self.quantity = quantity

    def __repr__(self):
        return f"InventoryItem(name='{self.name}', quantity={self.quantity})"

    def __add__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return InventoryItem(self.name, self.quantity + other.quantity)
        raise ValueError("Cannot add an item of different types.")

    def __sub__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            if self.quantity >= other.quantity:
                return InventoryItem(self.name, self.quantity - other.quantity)
            raise ValueError("Cannot subtract more than the available quantity.")
        raise ValueError("Cannot subtract the item of different types")

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return InventoryItem(self.name, int(self.quantity * factor))
        raise ValueError("Multiplication factor must be a number.")

    def __truediv__(self, factor):
        if isinstance(factor, (int, float)) and factor != 0:
            return InventoryItem(self.name, int(self.quantity / factor))
        raise ValueError("Division factor must be a non zero number.")

    def __eq__(self, other):
        if isinstance(other, InventoryItem):
            return self.name == other.name and self.quantity == other.quantity
        return False
    
    def __lt__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return self.quantity < other.quantity
        raise ValueError("cannot compare items of different types.")

    def __gt__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return self.quantity > other.quantity
        raise ValueError("cannot compare items of different types.")


item1 = InventoryItem("apple", 50)
item2 = InventoryItem("apple", 30)
item3 = InventoryItem("orange", 20)

add_res = item1 + item2
print(add_res)

sub_res = item1 - item2
print(sub_res)

mul_res = item1 * 2
print(mul_res)

div_res = item1 / 2
print(div_res)

print(item1 > item2)

print(item1 == InventoryItem("apple", 50))

try:
    add_inv_res  = item1 + item3
except ValueError as e:
    print(e)
