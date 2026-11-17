class Product:
    TAX_RATE = 0.13

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price

        if stock < 0:
            raise ValueError("Stock cannot be negative")

        self._stock = stock

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be greater than zero")

        self._price = round(value, 2)

    @property
    def stock(self):
        return self._stock

    def restock(self, qty):
        if qty <= 0:
            raise ValueError("Restock quantity must be positive")

        self._stock += qty

    def sell(self, qty):
        if qty <= 0:
            raise ValueError("Quantity must be positive")

        if qty > self._stock:
            raise ValueError("Not enough stock available")

        self._stock -= qty

    def describe(self):
        return f"{self.name}: Rs {self.price:.2f} ({self.stock} in stock)"

    def price_with_tax(self):
        return round(self.price * (1 + self.TAX_RATE), 2)

    @classmethod
    def from_string(cls, text):
        name, price, stock = text.split(",")
        return cls(name, float(price), int(stock))


class Cart:
    def __init__(self):
        self._items = []
        self._discount = 0

    @property
    def item_count(self):
        count = 0
        for item in self._items:
            count += item["qty"]
        return count

    def add(self, product, qty=1):
        product.sell(qty)

        for item in self._items:
            if item["product"] is product:
                item["qty"] += qty
                return

        self._items.append({
            "product": product,
            "qty": qty
        })

    def total(self):
        amount = 0
        for item in self._items:
            product = item["product"]
            qty = item["qty"]
            amount += product.price_with_tax() * qty

        amount *= 1 - self._discount / 100
        return round(amount, 2)

    def receipt(self):
        lines = []
        for item in self._items:
            product = item["product"]
            qty = item["qty"]
            subtotal = product.price_with_tax() * qty
            lines.append(f"{product.name} x{qty}  Rs {subtotal:.2f}")

        lines.append(f"TOTAL  Rs {self.total():.2f}")
        return "\n".join(lines)

    def apply_discount(self, percent):
        if percent < 0 or percent > 100:
            raise ValueError("Discount must be between 0 and 100")
        self._discount = percent


if __name__ == "__main__":
    pen = Product("Pen", 25, 10)
    book = Product("Book", 100, 5)

    print(pen.describe())
    pen.sell(3)
    print(pen.stock)

    book = Product.from_string("Book,100,5")
    print(book.price_with_tax())

    Product.TAX_RATE = 0.10
    print(book.price_with_tax())

    Product.TAX_RATE = 0.13

    pen = Product("Pen", 25, 10)
    book = Product("Book", 100, 5)

    cart = Cart()
    cart.add(pen, 2)
    cart.add(book)

    print(cart.item_count)
    print(cart.receipt())

    cart.apply_discount(10)
    print("After 10% discount:", cart.total())


# Part 4: Predict and Explain
#
# 1. Assigning -5 to pen.price raises a ValueError because the
#    price setter does not allow zero or negative values.
#    The original price remains unchanged.
#
# 2. It prints 999.
#    An underscore is a naming convention that tells programmers
#    an attribute is intended for internal use. It does not
#    completely prevent direct access or modification.
#
# 3. It prints 0.2 0.13.
#    Assigning TAX_RATE to object a creates an instance attribute
#    that overrides the class attribute for that object only.
#    Object b continues using the original class attribute.
#
# 4. Cart.add() should call product.sell() because the Product
#    class is responsible for managing its own stock.
#    This ensures that stock rules are checked before items
#    are added to the cart.
#
# 5. from_string() is a class method because it creates a new
#    Product object using the class itself.
#    It also keeps the object creation process organised
#    inside the Product class.
