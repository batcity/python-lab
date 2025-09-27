# Modules and Packages in Python 

Modules and packages are fundamental in Python for **organizing code, reusing functionality, and maintaining large projects**.

---

## What Are Modules?

A **module** is any Python file (`.py`) that contains code—functions, classes, or variables—that can be imported and reused in other Python programs.  

> **Important distinction:** While technically any `.py` file is a module, we usually use the term "module" for files that are **intended to be imported and reused**, rather than standalone scripts.

**Example**:

```python
# custom_module.py
def print_hello():
    print("Hello from a module!")
````

You can import it in another file:

```python
from custom_module import print_hello

print_hello()
```

**Why use modules?**

* Avoid code duplication
* Organize code logically
* Make projects easier to maintain and test

---

## What Are Packages?

A **package** is a collection of Python modules organized in a directory hierarchy. It allows **modular project organization**.

**Key points:**

* A package is a folder containing an `__init__.py` file (can be empty or execute initialization code)
* Modules inside a package can be imported individually or collectively

**Example structure**:

```
custom_package/
├── __init__.py       # Marks this folder as a package
└── custom_module.py  # A module inside the package
```

**Usage**:

```python
from custom_package import custom_module

custom_module.print_hello()
```

---

## Advanced Considerations

1. **Namespace Packages**

   * Python 3.3+ allows packages without `__init__.py` (namespace packages), enabling modules to span multiple directories.

2. **Absolute vs Relative Imports**

   * Absolute imports specify the full path from the project root.
   * Relative imports use `.` or `..` to reference sibling or parent modules within a package.

3. **Module Initialization (`__init__.py`)**

   * Can include code that runs when the package is imported.
   * Can expose selected submodules or functions using `__all__`.

4. **Reloading Modules**

   * Modules are loaded once per session. Use `importlib.reload(module)` to reload after changes.

5. **Package Organization Best Practices**

   * Keep modules focused on a single responsibility.
   * Group related modules logically into subpackages.
   * Avoid circular imports by careful module design.
