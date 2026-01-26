# Module 2 – SOLID Principles and Design Quality

This module focused on evaluating object-oriented design quality through the identification and refactoring of SOLID principle violations. The aim was to move beyond code that “works” and instead improve code that is maintainable, extensible, and robust under change.

The artefact demonstrates common design issues found in early or poorly structured object-oriented systems, such as excessive responsibilities within a single class, tight coupling, and limited flexibility when requirements evolve. Refactoring work addressed these issues by applying the SOLID principles in a practical and structured way. The Single Responsibility Principle was supported by separating concerns so that each class has a clear and focused purpose. The Open/Closed Principle was improved by introducing abstractions that allow new behaviour to be added without modifying existing code. Where inheritance was used, the design was reviewed to ensure compliance with the Liskov Substitution Principle, ensuring subclasses can be used safely through base-class interfaces.

This module strengthened my ability to analyse software designs critically and justify refactoring decisions using established principles. It also reinforced that good object-oriented design is not only about class creation, but about responsibility allocation, dependency management, and designing for change in a controlled and predictable way (Martin, 2003; Martin, 2008).

## Source Code

- [SOLID Principles – Design Violations and Refactored Solutions (view on GitHub)](https://github.com/olhaloshyna12/olhaloshyna12.github.io/blob/main/modules/module-02/module_2_SOLID_Principles_Design_Violations_and_Refactored_Solutions.py)

## References

Martin, R. C. (2003) *Agile Software Development: Principles, Patterns, and Practices*. Upper Saddle River, NJ: Prentice Hall.

Martin, R. C. (2008) *Clean Code: A Handbook of Agile Software Craftsmanship*. Upper Saddle River, NJ: Prentice Hall.
