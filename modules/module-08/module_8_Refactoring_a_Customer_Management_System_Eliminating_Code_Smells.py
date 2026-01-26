# Module 8 exercise was completed during an in-class seminar
#Refactoring a Customer Management System – Eliminating Code Smells
#Seminar 5 Task: Refactor a customer management system with long methods, duplicate code, and primitive obsession.
#The Problem: Smelly Customer Management System
code_smells_customer_system.py (Before Refactoring)
SMELL: Primitive Obsession - Representing everything with strings and lists.
customers = []
SMELL: Long Method, Duplicate Code - This function does too much and has repeated validation.
def add_customer(name, email, phone, street, city, postcode, country):
# Duplicate email validation logic
    if "@" not in email:
        print("Error: Invalid email format.")
        return
    # Duplicate phone validation logic (simplified)
    if not phone.startswith("+"):
        print("Error: Phone must be in international format (+XXX).")
        return
    # Check for duplicate email (more duplication would be here)
    for cust in customers:
        if cust['email'] == email:
            print("Error: Email already exists.")
            return
    # SMELL: Data Clump - street, city, postcode, country are always passed together.
    new_customer = {
        'name': name,
        'email': email,
        'phone': phone,
        'street': street,
        'city': city,
        'postcode': postcode,
        'country': country,
        'status': 'active' # SMELL: Magic String / Primitive Obsession for status
    }
    customers.append(new_customer)
    print(f"Customer {name} added successfully.")
# SMELL: Long Method, Feature Envy - This method is obsessed with the customer dictionary's structure.
def generate_customer_report():
    print("*** CUSTOMER REPORT ***")
    print("=======================")
    total = 0
    active_count = 0
    for customer in customers:
        total += 1
        # SMELL: Duplicate check for 'active' status
        if customer['status'] == 'active':
            active_count += 1
     # SMELL: Long block doing formatting based on internal structure
        address_line = f"{customer['street']}, {customer['city']}, {customer['postcode']}, {customer['country']}"
        print(f"Name: {customer['name']}")
        print(f"Email: {customer['email']}")
        print(f"Phone: {customer['phone']}")
        print(f"Address: {address_line}")
        print(f"Status: {customer['status']}")
        print("-" * 20)
    
    # SMELL: Calculation logic buried inside a reporting function
    print(f"Total Customers: {total}")
    print(f"Active Customers: {active_count}")
    print(f"Inactive Customers: {total - active_count}")
# SMELL: Duplicate Code - Same validation as in add_customer.
def update_customer_email(old_email, new_email):
    if "@" not in new_email:
        print("Error: Invalid email format.")
        return
    for customer in customers:
        if customer['email'] == old_email:
            customer['email'] = new_email
            print("Email updated.")
            return
    print("Error: Customer not found.")
# SMELL: Long Parameter List, Data Clump
def deactivate_customer(name, email, phone, street, city, postcode, country):
    for customer in customers:
        # SMELL: Fragile, long condition based on primitives.
        if (customer['name'] == name and customer['email'] == email and
            customer['phone'] == phone and customer['street'] == street and
            customer['city'] == city and customer['postcode'] == postcode and
            customer['country'] == country):
            customer['status'] = 'inactive' # Magic String
            print("Customer deactivated.")
            return
    print("Error: Customer not found.")
# Usage
add_customer("Alice", "alice@example.com", "+123456789", "123 Maple St", "Techville", "TV1 2AB", "UK")
add_customer("Bob", "bob@example.com", "+447777777777", "456 Oak Ave", "Codeburg", "CB2 3CD", "UK")
generate_customer_report()
Step-by-Step Refactoring Guide & Solution: 
Step 1: Introduce Classes to Cure Primitive Obsession
Create classes to encapsulate related data and behavior. This is the biggest and most important step.
from dataclasses import dataclass
from enum import Enum
# Use an Enum to eliminate Magic Strings for status
class CustomerStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
# Introduce Parameter Object for the Data Clump: Address
@dataclass
class Address:
    street: str
    city: str
    postcode: str
    country: str
    # Add behavior related to addresses
    def format_address(self):
        return f"{self.street}, {self.city}, {self.postcode}, {self.country}"
# The main Customer class, the core of our domain model
@dataclass
class Customer:
    name: str
    email: str
    phone: str
    address: Address  # Composing the Address object
    status: CustomerStatus = CustomerStatus.ACTIVE  # Use the Enum
    # Move validation methods INTO the class that owns the data
    def is_valid_email(self):
        return "@" in self.email
    def is_valid_phone(self):
        # More complex logic can go here later
        return self.phone.startswith("+")
Step 2: Create a Service Class to Manage Customers
This class handles the collection and operations like add, find, etc. It avoids using a global list.
class CustomerService:
    def __init__(self):
        self.customers = []  # Now a list of Customer objects, not dictionaries
    # Extract Method & Introduce Parameter Object: The long parameter list is now a single object.
    def add_customer(self, customer):
        # Delegate validation to the Customer class (may be better as a validator class)
        if not customer.is_valid_email():
            raise ValueError("Invalid email format.")
        if not customer.is_valid_phone():
            raise ValueError("Phone must be in international format (+XXX).")
        # Check for duplicate email
        # Extract Method for finding customer by email
        if self._find_customer_by_email(customer.email):
            raise ValueError("Email already exists.")
        self.customers.append(customer)
        print(f"Customer {customer.name} added successfully.")
    # Remove Duplicate Code: This logic is now in one place.
    def _find_customer_by_email(self, email):
        for customer in self.customers:
            if customer.email == email:
                return customer
        return None
    def update_customer_email(self, old_email, new_email):
        # Reuse the method to find the customer
        customer = self._find_customer_by_email(old_email)
        if not customer:
            raise ValueError("Customer not found.")
        # Create a temporary customer object to validate the new email? 
        # Or better: create a separate EmailValidator class.
        temp_customer = Customer("temp", new_email, "temp", None)
        if not temp_customer.is_valid_email():
            raise ValueError("Invalid new email format.")
        customer.email = new_email
        print("Email updated.")
    # Replace Parameter Clump with Customer object identity (usually you'd use an ID)
    def deactivate_customer(self, customer_email):
        customer = self._find_customer_by_email(customer_email)
        if customer:
            customer.status = CustomerStatus.INACTIVE
            print("Customer deactivated.")
        else:
            raise ValueError("Customer not found.")
Step 3: Create a Report Generator Class
This separates the concern of reporting from the concern of managing customers.
class CustomerReportGenerator:
    def __init__(self, customer_service):
        self.customer_service = customer_service
    # Break down the Long Method into smaller, well-named methods.
    def generate_report(self):
        self._print_header()
        self._print_customer_details()
        self._print_summary()
    def _print_header(self):
        print("*** CUSTOMER REPORT ***")
        print("=======================")
    def _print_customer_details(self):
        for customer in self.customer_service.customers:
            self._print_single_customer(customer)
    # The method now works with a Customer object's interface, not its internals.
    # This reduces Feature Envy.
    def _print_single_customer(self, customer):
        address_line = customer.address.format_address() # Delegate to Address class
        print(f"Name: {customer.name}")
        print(f"Email: {customer.email}")
        print(f"Phone: {customer.phone}")
        print(f"Address: {address_line}")
        print(f"Status: {customer.status.value}")
        print("-" * 20)
    # Extract Method for the summary calculations
    def _print_summary(self):
        total = len(self.customer_service.customers)
        # Use a generator expression for clarity
        active_count = sum(1 for customer in self.customer_service.customers if customer.status == CustomerStatus.ACTIVE)
        print(f"Total Customers: {total}")
        print(f"Active Customers: {active_count}")
        print(f"Inactive Customers: {total - active_count}")
Step 4: The Refactored Codebase in Action
refactored_customer_system.py (After Refactoring)
from dataclasses import dataclass
from enum import Enum
# DOMAIN MODEL
class CustomerStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
@dataclass
class Address:
    street: str
    city: str
    postcode: str
    country: str
    def format_address(self):
        return f"{self.street}, {self.city}, {self.postcode}, {self.country}"
@dataclass
class Customer:
    name: str
    email: str
    phone: str
    address: Address
    status: CustomerStatus = CustomerStatus.ACTIVE
    def is_valid_email(self):
        return "@" in self.email
    def is_valid_phone(self):
        return self.phone.startswith("+")
# SERVICE LAYER
class CustomerService:
    def __init__(self):
        self.customers = []
    def add_customer(self, customer):
        if not customer.is_valid_email():
            raise ValueError("Invalid email format.")
        if not customer.is_valid_phone():
            raise ValueError("Phone must be in international format (+XXX).")
        if self._find_customer_by_email(customer.email):
            raise ValueError("Email already exists.")
        self.customers.append(customer)
        print(f"Customer {customer.name} added successfully.")
    def _find_customer_by_email(self, email):
        for customer in self.customers:
            if customer.email == email:
                return customer
        return None
    # update_customer_email and deactivate_customer methods
# REPORTING MODULE
class CustomerReportGenerator:
    def __init__(self, customer_service):
        self.customer_service = customer_service
    def generate_report(self):
        self._print_header()
        self._print_customer_details()
        self._print_summary()
    def _print_header(self): ...
    def _print_customer_details(self): ...
    def _print_single_customer(self, customer): ...
    def _print_summary(self): ...
# USAGE
service = CustomerService()
report_generator = CustomerReportGenerator(service)
# Create Address and Customer objects
alice_address = Address("123 Maple St", "Techville", "TV1 2AB", "UK")
alice = Customer("Alice", "alice@example.com", "+123456789", alice_address)
bob_address = Address("456 Oak Ave", "Codeburg", "CB2 3CD", "UK")
bob = Customer("Bob", "bob@example.com", "+447777777777", bob_address)
# Use the service to manage customers
try:
    service.add_customer(alice)
    service.add_customer(bob)
    report_generator.generate_report()
except ValueError as e:
    print(f"Error: {e}")
