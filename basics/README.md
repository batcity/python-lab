# Type Casting in Python

Type casting is the process of converting a value from one data type to another.

Python supports two types of type casting:

1. **Implicit Type Casting (Type Conversion)**
   - Done automatically by Python.
   - Usually occurs when mixing compatible data types in expressions.
   - Example:
     ```python
     x = 5       # int
     y = 2.5     # float
     z = x + y   # x is implicitly converted to float
     print(z)    # Output: 7.5
     ```

2. **Explicit Type Casting (Type Conversion)**
   - Done manually by the programmer using built-in functions.
   - Common functions: `int()`, `float()`, `str()`
   - Example:
     ```python
     x = "10"
     y = int(x)  # explicitly converting string to integer
     print(y + 5)  # Output: 15
     ```