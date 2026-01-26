# Module 1 – Object-Oriented Design Foundations

This module introduced the foundational principles of object-oriented programming and established the conceptual basis for all subsequent work in the Advanced Object-Oriented Design and Programming module. The focus extended beyond writing functional code to understanding how object-oriented thinking supports clarity, maintainability, and extensibility in software systems.

The practical exercise involved the design and implementation of a vehicle management system using a class hierarchy. A base `Vehicle` class was created to define shared attributes and behaviours common to all vehicles, while concrete subclasses such as `Car`, `Bike`, and `Truck` extended this base class to represent specialised vehicle types.

Key object-oriented principles were applied throughout the design. Abstraction was used to capture common vehicle behaviour in the base class, reducing duplication and improving clarity. Encapsulation ensured that internal state was protected and could only be accessed or modified through controlled methods, helping to maintain valid object states. Inheritance was used to model clear “is-a” relationships between vehicle types, while polymorphism allowed different vehicle objects to be treated uniformly through a shared interface.

This module was particularly valuable in shifting my approach from procedural thinking to responsibility-driven design. Rather than focusing on isolated functions, I learned to consider how responsibilities should be distributed across classes and how design decisions impact long-term maintainability. The concepts introduced here formed the foundation for later modules on SOLID principles, design patterns, refactoring, and large-scale system architecture.

## Source Code

- [Vehicle Management System – Object-Oriented Class Hierarchy](https://github.com/olhaloshyna12/olhaloshyna12.github.io/blob/main/modules/module-01/module_1_Vehicle_Management_System_Object_Oriented_Class_Hierarchy.py)

## References

Gamma, E., Helm, R., Johnson, R. and Vlissides, J. (1994) *Design Patterns: Elements of Reusable Object-Oriented Software*. Reading, MA: Addison-Wesley.

Martin, R. C. (2003) *Agile Software Development: Principles, Patterns, and Practices*. Upper Saddle River, NJ: Prentice Hall.

Martin, R. C. (2008) *Clean Code: A Handbook of Agile Software Craftsmanship*. Upper Saddle River, NJ: Prentice Hall.
