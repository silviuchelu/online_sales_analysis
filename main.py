from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()
manager.add_product(Product("Laptop", 3000, 5))
manager.add_product(Product("Mouse", 100, 10))
manager.add_product(Product("Tastatură", 200, 7))

print("Produse disponibile:")
manager.display_products()

print("\nValoarea totală a inventarului:", manager.total_inventory_value(), "RON")

print("\nȘtergem produsul 'Mouse'...")
manager.remove_product("Mouse")

print("Produse disponibile după ștergere:")
manager.display_products()

cart = Cart()
cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[1])
cart.add_to_cart(manager.products[2])

print("\nCoșul de cumpărături:")
cart.display_cart()
print("Total de plată:", cart.total_cart_value(), "RON")
