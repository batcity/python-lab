# Note: You don't need this import from version 3.13 onwards
from __future__ import annotations

class Node:
    
    def __init__(self, next: Node | None):
        self.next = next
        
node = Node(None)
print(node)
print(node.next)