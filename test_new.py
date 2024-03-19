import unittest

class Product:
    def __init__(self, name, price, quantity):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a numeric value")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.name = name
        self.price = price
        self.quantity = quantity
    

    
    def calculateTotal(self):
        return self.price * self.quantity

class TestProduct(unittest.TestCase):

    def test_calculateTotal(self):
        with self.assertRaises(ValueError):
            
            product = Product("Test Product", 10, -3)  