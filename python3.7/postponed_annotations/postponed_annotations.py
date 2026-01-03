from __future__ import annotations

class Node:
    
    def __init__(self, next: Node | None):
        self.next = next
        
node = Node(None)
print(node)
print(node.next)