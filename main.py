from product import Product
from product_manager import ProductManager

manager = ProductManager()
manager.add_product(Product("Laptop", 3000, 5))
manager.add_product(Product("Mouse", 100, 10))
manager.add_product(Product("Tastatură", 200, 7))

print("Produse disponibile:")
manager.display_products()

print("\nValoarea totală a inventarului:", manager.total_inventory_value(), "RON")
