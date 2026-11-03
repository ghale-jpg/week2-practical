
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

    def is_long(self):
        return self.pages > 300

    def reading_time(self, pages_per_hour):
        hours = self.pages / pages_per_hour
        return int(hours) if hours == int(hours) else int(hours) + 1


b1 = Book("Dune", "Frank Herbert", 412)
b2 = Book("The Little Prince", "Antoine de Saint-Exupery", 96)

print(b1.describe())
print(b2.describe())
print(b1.is_long(), b2.is_long())
