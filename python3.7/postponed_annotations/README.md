# Postponed Annotations:

Before Python 3.13, forward references in type annotations required special handling.

For example, a class that refers to itself:

```python
class Node:
    
    def __init__(self, next: Node | None):
        self.next = next
```


In Python 3.12 and earlier, this would raise a NameError unless you either:
wrapped the type in quotes ("Node"), or
enabled postponed evaluation of annotations:
from __future__ import annotations
This allows the Node type to be referenced without quotes.

Python 3.13+

Starting in Python 3.13, annotations are evaluated lazily by default.
Forward references work automatically, and the __future__ import is no longer required.