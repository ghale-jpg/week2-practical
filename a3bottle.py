
class WaterBottle:
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0
        self.refill_count = 0

    def fill(self, ml):
        if self.amount == 0 and ml > 0:
            self.refill_count += 1

        self.amount += ml

        if self.amount > self.capacity:
            self.amount = self.capacity

    def drink(self, ml):
        if self.amount >= ml:
            self.amount -= ml
            return True
        return False

    def percent_full(self):
        return round((self.amount / self.capacity) * 100)

    def empty(self):
        self.amount = 0

    def is_empty(self):
        return self.amount == 0

    def refills(self):
        return self.refill_count


bottle = WaterBottle(750)

bottle.fill(500)
print(bottle.amount)

bottle.fill(400)
print(bottle.amount)

print(bottle.drink(200), bottle.amount)
print(bottle.drink(600), bottle.amount)
print(bottle.percent_full())

bottle.empty()
print(bottle.amount, bottle.is_empty())
