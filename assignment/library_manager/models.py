from abc import ABC, abstractmethod

class LibraryItem(ABC):
    total_items = 0  # class attribute, shared by every item

    def __init__(self, title, item_id):          # fix: was `init`
        self.title = title
        self.item_id = item_id
        self.__available = True                   # private
        LibraryItem.total_items += 1              # update class attribute

    def is_available(self):
        return self.__available

    def mark_borrowed(self):
        self.__available = False                  # fix: was `pass`

    def mark_returned(self):
        self.__available = True                   # fix: was `pass`

    @abstractmethod
    def late_fee(self, days_late):
        pass  # every child class must implement this


class Book(LibraryItem):
    DAILY_RATE = 2

    def __init__(self, title, item_id, author):  # fix: was `init`
        super().__init__(title, item_id)
        self.author = author

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        return f"Book: {self.title} by {self.author} (ID {self.item_id})"

# TODO: class Magazine(LibraryItem): rate 1, extra field issue_number
# TODO: class DVD(LibraryItem): rate 5, extra field duration_minutes


class Member:

    def __init__(self, name, member_id, max_items=3):  # fix: was `init`
        self.name = name
        self.member_id = member_id
        self.max_items = max_items
        self.__borrowed = []                      # private list of items

    def borrow(self, item):
        if not item.is_available():               # fix: was pass
            raise ValueError(f"'{item.title}' is not available.")
        if len(self.__borrowed) >= self.max_items:
            raise ValueError(f"{self.name} has reached the borrow limit of {self.max_items}.")
        item.mark_borrowed()
        self.__borrowed.append(item)

    def return_item(self, item, days_late=0):
        if item not in self.__borrowed:           # fix: was pass
            raise ValueError(f"'{item.title}' was not borrowed by {self.name}.")
        item.mark_returned()
        self.__borrowed.remove(item)
        return item.late_fee(days_late)

    def borrowed_titles(self):
        return [item.title for item in self.__borrowed]
