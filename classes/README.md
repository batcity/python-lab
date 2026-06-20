# Classes

Classes provide a means of bundling data and functionality together.

## Why Use Classes? (The Power of OOP)


In simple terms, classes bundle data (attributes) and functionality (methods) together into a single, organized package.

Without classes, variables and functions float around independently, which quickly leads to disorganized "spaghetti code" as a project grows.

### Key Benefits

- **Intuitive Modeling:** Classes mirror the real world. Instead of managing a random variable car_color and a separate function paint_car(), you create a Car object that has a color and knows how to be painted.

- **🔒 Encapsulation (Security):** By bundling data and functions, you protect the internal state of your object. For example, in a BankAccount class, outside code cannot arbitrarily change the balance variable; it must go through the safety checks inside the deposit() or withdraw() methods.

- **Reusability (The Blueprint Concept):** A class acts as a template. You write the code once (e.g., an Enemy class for a game), and you can instantly instantiate hundreds of individual copies (instances), each tracking its own health and position independently.

- **Easier Maintenance:** Classes make code modular. If there is a bug with user authentication, you know exactly which file and class to look at, rather than hunting through scattered global variables.