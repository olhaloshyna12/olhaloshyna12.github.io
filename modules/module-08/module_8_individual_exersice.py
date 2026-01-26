#Module 8 Individual Assignment: Refactoring Code for Maintainability
# #This collaborative discussion involved analysing a given Python code snippet to identify refactoring opportunities that improve readability and maintainability. The task focused on identifying common code smells, including magic numbers and long conditional logic, and suggesting appropriate refactoring techniques. Two approaches were proposed: replacing magic numbers with constants and applying the Strategy Pattern to improve extensibility while keeping the program behaviour unchanged.
def calculate_total_price(items):
    total = 0
    for item in items:
        if item['type'] == 'book':
            total += item['price'] * 0.9 # 10% discount for books
        elif item['type'] == 'electronics':
            total += item['price'] * 0.8 # 20% discount for electronics
        else:
            total += item['price']
    return total
BOOK_DISCOUNT = 0.9
ELECTRONICS_DISCOUNT = 0.8

def calculate_total_price(items):
    total = 0
    for item in items:
        if item["type"] == "book":
            total += item["price"] * BOOK_DISCOUNT
        elif item["type"] == "electronics":
            total += item["price"] * ELECTRONICS_DISCOUNT
        else:
            total += item["price"]
    return total
class DiscountStrategy:
    def apply(self, price):
        return price

class BookDiscount(DiscountStrategy):
    def apply(self, price):
        return price * 0.9

class ElectronicsDiscount(DiscountStrategy):
    def apply(self, price):
        return price * 0.8

STRATEGIES = {
    "book": BookDiscount(),
    "electronics": ElectronicsDiscount()
}

def calculate_total_price(items):
    total = 0
    for item in items:
        strategy = STRATEGIES.get(item["type"], DiscountStrategy())
        total += strategy.apply(item["price"])
    return total