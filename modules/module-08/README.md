# Module 8 – Refactoring and Clean Code

This module focused on improving software quality through disciplined refactoring and the application of clean code principles. Rather than introducing new functionality, the emphasis was on restructuring existing code to improve readability, maintainability, and architectural clarity while preserving external behaviour.

Refactoring was approached as a continuous and systematic activity, highlighting its importance in professional software development. The module combined an individual refactoring exercise with a larger, more complex system-level refactoring task.

---

## Individual Refactoring Exercise

The individual exercise introduced small-scale refactoring techniques aimed at improving code structure without altering functionality. Common issues such as unclear naming, unnecessarily complex logic, and poorly distributed responsibilities were addressed through incremental changes.

This exercise reinforced the importance of making small, safe refactoring steps and demonstrated how even minor improvements can significantly enhance code readability and maintainability. It also strengthened my understanding of how clean code practices support long-term system evolution.

### Source Code

- [Individual Refactoring Exercise (view on GitHub)](https://github.com/olhaloshyna12/olhaloshyna12.github.io/blob/main/modules/module-08/module_8_individual_exersice.py)

---

## Refactoring a Customer Management System – Eliminating Code Smells

The larger refactoring task involved transforming a procedurally structured customer management system containing multiple code smells into a well-structured object-oriented design. The original implementation exhibited issues such as long methods, duplicated logic, primitive obsession, and unclear separation of responsibilities.

Refactoring activities introduced cohesive domain models to represent core business concepts and service layers to separate business logic from data handling. Responsibilities were redistributed across classes to improve cohesion and reduce coupling. Each refactoring step was validated to ensure that existing behaviour remained unchanged, reinforcing the importance of correctness during structural change.

This artefact demonstrated advanced refactoring skills and architectural reasoning. It highlighted the relationship between clean code practices and system scalability, showing how improving internal structure prepares systems for future extension and integration with more complex or data-driven components.

### Source Code

- [Customer Management System Refactoring – Eliminating Code Smells (view on GitHub)](https://github.com/olhaloshyna12/olhaloshyna12.github.io/blob/main/modules/module-08/module_8_Refactoring_a_Customer_Management_System_Eliminating_Code_Smells.py)

---

## References

Fowler, M. (2018) *Refactoring: Improving the Design of Existing Code*. 2nd edn. Boston, MA: Addison-Wesley.

Martin, R. C. (2008) *Clean Code: A Handbook of Agile Software Craftsmanship*. Upper Saddle River, NJ: Prentice Hall.
