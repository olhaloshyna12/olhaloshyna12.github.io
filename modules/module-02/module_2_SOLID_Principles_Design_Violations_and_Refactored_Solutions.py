# Module 2 exercise was completed during an in-class seminar
#SOLID Principles – Design Violations and Refactored Solutions
#Advanced Object-Oriented Design & Programming (AOODP)
#Single Responsibility Principle (SRP) – File Handling 
#SRP Violation: One class reads AND processes files.
class FileManager:
    def read_file(self, path):
        with open(path, 'r') as f:
            return f.read()
    def count_words(self, text):
        return len(text.split())
	# SRP Complaint: Split into two classes
class FileReader:
    def read_file(self, path):
        with open(path, 'r') as f:
            return f.read()
class WordCounter:
    def count_words(self, text):
        return len(text.split())
#Open/Closed Principle (OCP) – Payment Processor
# OCP Violation: Adding PayPal requires modifying `process_payment()`.
class PaymentProcessor:
    def process_payment(self, amount, method):
        if method == "CreditCard":
            print(f"Processing ${amount} via Credit Card")
        elif method == "Stripe":
            print(f"Processing ${amount} via Stripe")
# OCP Complaint: Use abstractions 
class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount):
        pass
class CreditCard(PaymentMethod):
    def process(self, amount):
        print(f"Processing ${amount} via Credit Card")
class Stripe(PaymentMethod):
    def process(self, amount):
        print(f"Processing ${amount} via Stripe")
# Add PayPal by creating `PayPal(PaymentMethod)`.
#Liskov Substitution Principle (LSP) – Bird-Fly Dilemma 
# LSP Violation: Penguin can't fly, but inherits from Bird.
class Bird:
    def fly(self):
        print("Flying!")
class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")   # Violates LSP!
#LSP Compliant: Split into Flyable and NonFlyable birds.
class Bird:
    pass
class FlyingBird(Bird):
    def fly(self):
        print("Flying!")
class Penguin(Bird):
    pass  		# No fly() method!
#Interface Segregation Principle (ISP): User Roles 
# ISP Violation: All users must implement `admin_methods()`.
class User(ABC):
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def admin_methods(self):
        pass
# ISP Compliant: Split interfaces.
class BasicUser(ABC):
    @abstractmethod
    def login(self):
        pass
class AdminUser(BasicUser):
    @abstractmethod
    def admin_methods(self):
        pass
#Dependency Inversion Principle (DIP): Payment Processing 
# DIP Violation: Direct dependency on Stripe.
class PaymentProcessor:
    def __init__(self):
        self.stripe = Stripe()
    def pay(self, amount):
        self.stripe.charge(amount)
# DIP Compliant: Depend on abstraction.
class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, amount):
        pass
class StripeGateway(PaymentGateway):
    def charge(self, amount):
        print(f"Charging ${amount} via Stripe")
class PayPalGateway(PaymentGateway):
    def charge(self, amount):
        print(f"Charging ${amount} via PayPal")
class PaymentProcessor:
    def __init__(self, gateway: PaymentGateway):
        self.gateway = gateway
    def pay(self, amount):
        self.gateway.charge(amount)
