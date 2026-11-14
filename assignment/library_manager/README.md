# Library Manager

## How to run

Requires Python 3.12 or later. No external packages are needed.

```bash
python3 main.py        
```

## Files

| File | Purpose |
|------|---------|
| `models.py` | `LibraryItem` (abstract parent), `Book`, `Magazine`, `DVD` and `Member` |
| `main.py` | Demo that runs every feature and prints the results |
| `output.txt` | Console output of the final run |

## Late fees

| Item | Rate per day | 3 days late |
|------|--------------|-------------|
| Book | Rs 2 | Rs 6 |
| Magazine | Rs 1 | Rs 3 |
| DVD | Rs 5 | Rs 15 |

## Reflection

**1. Why is `LibraryItem` abstract, and what happens if `DVD` forgets to write `late_fee()`?**

`LibraryItem` is abstract because it only describes what every library item has in common. A plain "item" with no type has no late-fee rate, so creating one would make no sense. Because `late_fee()` is marked with `@abstractmethod`, a `DVD` class without its own `late_fee()` would also stay abstract. Python would then raise a `TypeError` as soon as you try to create a DVD, so the mistake shows up right away instead of later when a fee is calculated.

**2. What happens when you read `item.__available` from outside the class, and why do we use `is_available()` instead?**

Reading `item.__available` from outside the class raises an `AttributeError`. Python name-mangles attributes that start with two underscores, so inside the class the attribute is actually stored as `_LibraryItem__available`. We use `is_available()` because it gives read-only access through the class's public interface. Availability can then only change through `mark_borrowed()` and `mark_returned()`, so outside code can't put an item into an invalid state.

**3. What is the difference between `LibraryItem.total_items` and `self.title`?**

`LibraryItem.total_items` is a class attribute. There is one copy shared by every item, and it counts how many items have been created in total. `self.title` is an instance attribute. Each object stores its own title, so changing one book's title has no effect on any other item.
