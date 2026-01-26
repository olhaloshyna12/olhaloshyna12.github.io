# Module 6 – Concurrency and Parallelism

This module addressed concurrency and parallelism, focusing on the challenges that arise when multiple threads operate on shared resources. The emphasis was on designing object-oriented systems that remain correct, secure, and robust under non-deterministic execution.

Concurrency introduces risks that are not present in single-threaded programs, such as race conditions, lost updates, and deadlocks. This module combined exploratory seminar exercises with an assessed capstone artefact to develop both conceptual understanding and practical implementation skills.

---

## Concurrency and Parallelism – Seminar Exercises

The seminar exercises explored common concurrency problems through small, focused examples. These exercises demonstrated how unsynchronised access to shared state can lead to inconsistent behaviour and subtle bugs that are difficult to detect through casual testing.

Encapsulation was used to restrict direct access to shared data, while synchronisation mechanisms were introduced to control concurrent access. These exercises emphasised the importance of clear responsibility separation and careful design when working with parallel execution. The seminar work provided essential preparation for the more complex assessed task completed later in the module.

### Source Code

- [Concurrency and Parallelism – Seminar Exercises (view on GitHub)](https://github.com/olhaloshyna12/olhaloshyna12.github.io/blob/main/modules/module-06/module_6_Concurrency_and_Parallelism.py)

---

## Assessed Capstone Project – Thread-Safe Banking System

The assessed capstone project required the design and implementation of a secure, thread-safe banking system capable of handling multiple concurrent transactions. The primary objective was to ensure that account balances remained consistent and correct under parallel execution.

The system was designed using clear object-oriented principles, with separate responsibilities for account management, transaction processing, and execution control. Encapsulation protected sensitive account state, ensuring that balance updates occurred only through controlled methods. Synchronisation mechanisms were applied to guarantee atomicity of transactions and prevent race conditions when multiple threads attempted to modify shared resources simultaneously.

Particular attention was given to deadlock prevention through consistent lock ordering and disciplined access patterns. This required careful reasoning about thread interleavings and potential failure scenarios. Iterative testing was used to validate correctness under concurrent execution and to identify subtle defects.

This artefact demonstrates advanced understanding of secure coding practices, concurrency control, and robust object-oriented design in a realistic, safety-critical context. It highlights how design decisions at the class and method level directly affect system reliability and data integrity.

### Source Code

- [Assessed Capstone Project – Thread-Safe Banking System (view on GitHub)](https://github.com/olhaloshyna12/olhaloshyna12.github.io/blob/main/modules/module-06/module_6_assignment_Capstone_Project.py)

---

## References

Goetz, B. et al. (2006) *Java Concurrency in Practice*. Boston, MA: Addison-Wesley.

Martin, R. C. (2008) *Clean Code: A Handbook of Agile Software Craftsmanship*. Upper Saddle River, NJ: Prentice Hall.
