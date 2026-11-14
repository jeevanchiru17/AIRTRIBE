from models import Book, Member, Magazine, DVD  # TODO: also import Magazine, DVD
book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Monthly", 2, 15)
dvd = DVD("Inception", 3, 148)


# TODO: create one Magazine and one DVD
alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# 1. Borrowing with error handling
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())

    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)


# 2. TODO: trigger the borrow-limit error and the not-borrowed error, catching each

try:
    bob.borrow(magazine)
    bob.borrow(dvd)  # Exceeds limit of 1
except ValueError as e:
    print("Borrow limit error:", e)

# 3. Polymorphism: one loop, no type checks
items = [book, magazine, dvd]  # TODO: add the magazine and the DVD

try:
    bob.return_item(book)
except ValueError as e:
    print("Return error:", e)

for item in items:

    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

# 4. Class attribute shared by all objects
print("Total items created:", Book.total_items)


