# Design Table
#
# Question                         | Your Answer
# ------------------------------------------------------------
# What is the thing?               | A shopping cart belonging to one customer.
# What does it know?               | Owner name and a list of shopping items.
# What can it do?                  | Add items, remove items, count units and calculate total.
# What starts empty or at zero?    | The items list starts empty.
# What should never be allowed?   | Different customers should not share the same cart.


class ShoppingCart:
    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def add_item(self, name, price, qty=1):
        for item in self.items:
            if item["name"] == name:
                item["qty"] += qty
                return

        self.items.append({
            "name": name,
            "price": price,
            "qty": qty
        })

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return

    def item_count(self):
        count = 0

        for item in self.items:
            count += item["qty"]

        return count

    def total(self):
        amount = 0

        for item in self.items:
            amount += item["price"] * item["qty"]

        return amount

    def receipt(self):
        for item in self.items:
            print(item["name"], item["price"], "x", item["qty"])

        print("Total:", self.total())


cart = ShoppingCart("Asha")

cart.add_item("Notebook", 120, 3)
cart.add_item("Pen", 25, 4)
cart.add_item("Bag", 1500)

print(cart.item_count(), cart.total())

cart.remove_item("Bag")

print(cart.item_count(), cart.total())

other = ShoppingCart("Ravi")

print(other.owner, other.item_count(), other.total())
