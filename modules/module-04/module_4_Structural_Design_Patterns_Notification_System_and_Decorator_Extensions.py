# Module 4 exercise was completed during an in-class seminar
#Structural Design Patterns – Notification System and Decorator Extensions
#Q1: How Structural Design Patterns Enable Modular and Flexible Code? 
#Ans: Creating a notification system that demonstrates multiple structural patterns working together to create modular, flexible code. 
from abc import ABC, abstractmethod
# Adapter Pattern: Standardize different notification services
class NotificationService(ABC):
    @abstractmethod
    def send(self, message: str):
        pass
# Adaptee 1: Email service with incompatible interface
class EmailService:
    def send_email(self, recipient, subject, body):
        return f"Email to {recipient}: {subject} - {body}"
# Adaptee 2: SMS service with incompatible interface  
class SMSService:
    def send_sms(self, phone_number, text):
        return f"SMS to {phone_number}: {text}"
# Adapter for EmailService
class EmailAdapter(NotificationService):
    def __init__(self, email_service, recipient):
        self.email_service = email_service
        self.recipient = recipient
    
    def send(self, message):
        return self.email_service.send_email(self.recipient, "Notification", message)
# Adapter for SMSService
class SMSAdapter(NotificationService):
    def __init__(self, sms_service, phone_number):
        self.sms_service = sms_service
        self.phone_number = phone_number
    
    def send(self, message):
        return self.sms_service.send_sms(self.phone_number, message)
# Decorator Pattern: Add functionality dynamically
class NotificationDecorator(NotificationService):
    def __init__(self, notification_service):
        self.notification_service = notification_service
    
    def send(self, message):
        return self.notification_service.send(message)
# Concrete Decorator: Add timestamp
class TimestampDecorator(NotificationDecorator):
    def send(self, message):
        from datetime import datetime
        timestamped_msg = f"[{datetime.now()}] {message}"
        return self.notification_service.send(timestamped_msg)
# Concrete Decorator: Add priority tagging
class PriorityDecorator(NotificationDecorator):
    def __init__(self, notification_service, priority="Medium"):
        super().__init__(notification_service)
        self.priority = priority
    
    def send(self, message):
        prioritized_msg = f"[{self.priority}] {message}"
        return self.notification_service.send(prioritized_msg)
# Facade Pattern: Simple interface for complex system
class NotificationFacade:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SMSService()
    
    def create_email_notifier(self, email):
        return EmailAdapter(self.email_service, email)
    
    def create_sms_notifier(self, phone_number):
        return SMSAdapter(self.sms_service, phone_number)
    
    def send_urgent_email(self, email, message):
        notifier = self.create_email_notifier(email)
        notifier = PriorityDecorator(notifier, "High")
        notifier = TimestampDecorator(notifier)
        return notifier.send(message)
# Client code
if __name__ == "__main__":
    # Create facade
    notification_system = NotificationFacade()
    
    # Create different notification channels
    email_notifier = notification_system.create_email_notifier("user@example.com")
    sms_notifier = notification_system.create_sms_notifier("+1234567890")
    
    # Send basic notifications
    print("Basic notifications:")
    print(email_notifier.send("Your order has shipped!"))
    print(sms_notifier.send("Your package will arrive tomorrow"))
    
    # Decorate notifications dynamically
    print("\nDecorated notifications:")
    urgent_email = PriorityDecorator(email_notifier, "High")
    urgent_email = TimestampDecorator(urgent_email)
    print(urgent_email.send("Server down!"))
    
    timed_sms = TimestampDecorator(sms_notifier)
    print(timed_sms.send("Meeting reminder"))
    
    # Use facade's simplified method
    print("\nUsing facade simplified method:")
    print(notification_system.send_urgent_email("admin@example.com", "Critical error detected"))
#Q2: Implement the Decorator Pattern in Python to enhance the functionality of an existing class. 
#Q3: Create a coffee shop application where you can dynamically add toppings (e.g., milk, sugar) to a base coffee object. 
#Ans: Simple Coffee Shop Example (covers both questions 2 and 3). 
# The Base Component Interface
class Coffee:
    def cost(self):
        return 5  # Base price of simple coffee
    
    def description(self):
        return "Simple coffee"
# Base Decorator
class CoffeeDecorator:
    def __init__(self, coffee):
        self._coffee = coffee  # Reference to the wrapped coffee object
    
    def cost(self):
        return self._coffee.cost()
    
    def description(self):
        return self._coffee.description()
# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2  # Add $2 for milk
    
    def description(self):
        return self._coffee.description() + ", milk"
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1  # Add $1 for sugar
    
    def description(self):
        return self._coffee.description() + ", sugar"
class ChocolateDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 3  # Add $3 for chocolate
    
    def description(self):
        return self._coffee.description() + ", chocolate"
# Usage Example
if __name__ == "__main__":
    # Start with simple coffee
    my_coffee = Coffee()
    print(f"Base: {my_coffee.description()} - ${my_coffee.cost()}")
    
    # Add milk
    my_coffee = MilkDecorator(my_coffee)
    print(f"With milk: {my_coffee.description()} - ${my_coffee.cost()}")
    
    # Add sugar
    my_coffee = SugarDecorator(my_coffee)
    print(f"With milk & sugar: {my_coffee.description()} - ${my_coffee.cost()}")
    
    # Add chocolate
    my_coffee = ChocolateDecorator(my_coffee)
    print(f"Deluxe: {my_coffee.description()} - ${my_coffee.cost()}")
    
    print("\n" + "="*40)
    
    # Create different combinations
    print("Different coffee combinations:")
    
    # Just sugar
    coffee1 = SugarDecorator(Coffee())
    print(f"Sugar coffee: {coffee1.description()} - ${coffee1.cost()}")
    
    # Milk and chocolate
    coffee2 = ChocolateDecorator(MilkDecorator(Coffee()))
    print(f"Mocha: {coffee2.description()} - ${coffee2.cost()}")
    
    # Everything!
    coffee3 = ChocolateDecorator(SugarDecorator(MilkDecorator(Coffee())))
    print(f"Everything: {coffee3.description()} - ${coffee3.cost()}")
