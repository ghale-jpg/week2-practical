products = {
    "P101": {"name": "Keyboard", "price": 1800.0, "stock": 10},
    "P102": {"name": "Mouse", "price": 900.0, "stock": 15},
    "P103": {"name": "Headphones", "price": 2500.0, "stock": 8},
    "P104": {"name": "USB Drive", "price": 1200.0, "stock": 20},
    "P105": {"name": "Monitor", "price": 18000.0, "stock": 5},
    "P106": {"name": "Webcam", "price": 3500.0, "stock": 7}
}
cart = {}

def display_products():
    print("\nID     Product             Price (Rs.)     Stock")
    for product_id, product in products.items():
        print(f"{product_id:<6} {product['name']:<19} {product['price']:<14.2f} {product['stock']}")

def get_quantity(prompt):
    while True:
        try:
            quantity = int(input(prompt))
            if quantity > 0:
                return quantity
            print("Quantity must be greater than zero.")
        except ValueError:
            print("Enter a valid whole number.")

def add_to_cart():
    product_id = input("Enter product ID: ").strip().upper()
    if product_id not in products:
        print("Product not found.")
        return
    quantity = get_quantity("Enter quantity: ")
    current_quantity = cart.get(product_id, 0)
    if current_quantity + quantity > products[product_id]["stock"]:
        print("Not enough stock available.")
        return
    cart[product_id] = current_quantity + quantity
    print("Product added to cart.")

def remove_from_cart():
    product_id = input("Enter product ID to remove: ").strip().upper()
    if product_id in cart:
        del cart[product_id]
        print("Product removed from cart.")
    else:
        print("Product is not in the cart.")

def update_quantity():
    product_id = input("Enter product ID to update: ").strip().upper()
    if product_id not in cart:
        print("Product is not in the cart.")
        return
    quantity = get_quantity("Enter new quantity: ")
    if quantity > products[product_id]["stock"]:
        print("Not enough stock available.")
        return
    cart[product_id] = quantity
    print("Cart quantity updated.")

def calculate_subtotal():
    subtotal = 0
    for product_id, quantity in cart.items():
        subtotal += products[product_id]["price"] * quantity
    return subtotal

def get_discount_rate(subtotal):
    if subtotal >= 20000:
        return 0.15
    elif subtotal >= 10000:
        return 0.10
    elif subtotal >= 5000:
        return 0.05
    return 0

def display_invoice():
    if not cart:
        print("Your cart is empty.")
        return
    subtotal = calculate_subtotal()
    discount_rate = get_discount_rate(subtotal)
    discount = subtotal * discount_rate
    discounted_total = subtotal - discount
    vat = discounted_total * 0.13
    final_total = discounted_total + vat
    print("\n================ INVOICE ================")
    print(f"{'Product':<18}{'Qty':>5}{'Unit Price':>14}{'Line Total':>15}")
    for product_id, quantity in cart.items():
        product = products[product_id]
        line_total = product["price"] * quantity
        print(f"{product['name']:<18}{quantity:>5}{product['price']:>14.2f}{line_total:>15.2f}")
    print("-----------------------------------------")
    print(f"Subtotal:                 Rs. {subtotal:.2f}")
    print(f"Discount ({discount_rate * 100:.0f}%):          Rs. {discount:.2f}")
    print(f"VAT (13%):                Rs. {vat:.2f}")
    print(f"Final bill:               Rs. {final_total:.2f}")
    print("=========================================")

def checkout():
    if not cart:
        print("Cannot checkout because the cart is empty.")
        return
    display_invoice()
    confirm = input("Confirm purchase? (y/n): ").strip().lower()
    if confirm == "y":
        for product_id, quantity in cart.items():
            products[product_id]["stock"] -= quantity
        cart.clear()
        print("Purchase successful. Stock has been updated.")
    else:
        print("Purchase cancelled. Your cart has been kept.")

def main():
    while True:
        print("\n===== SHOPPING CART AND BILLING SYSTEM =====")
        print("1. Display products")
        print("2. Add product to cart")
        print("3. Remove product from cart")
        print("4. Update cart quantity")
        print("5. Display invoice")
        print("6. Checkout")
        print("7. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            display_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            update_quantity()
        elif choice == "5":
            display_invoice()
        elif choice == "6":
            checkout()
        elif choice == "7":
            print("Thank you for shopping.")
            break
        else:
            print("Invalid choice. Please select 1-7.")

if __name__ == "__main__":
    main()
