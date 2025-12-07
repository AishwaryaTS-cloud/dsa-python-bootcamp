# Basic Linked List Implementation — Node creation + manual connections

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


# --------------------------------------------
# Example: Manually creating and connecting nodes
# --------------------------------------------

# Create nodes
n1 = Node(3)
n2 = Node(7)
n3 = Node(2)
n4 = Node(9)

# Connect nodes
n1.next = n2
n2.next = n3
n3.next = n4

# Create linked list and assign head
ll = LinkedList()
ll.head = n1

# --------------------------------------------
# Simple traversal
# --------------------------------------------
current = ll.head
while current:
    print(current.value)
    current = current.next


# --------------------------------------------
# Doubly Linked List Node Example
# --------------------------------------------

class DNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Example doubly nodes
d1 = DNode(3)
d2 = DNode(7)

# connect
d1.next = d2
d2.prev = d1

print("Doubly forward:", d1.value, "->", d1.next.value)
print("Doubly backward:", d2.value, "->", d2.prev.value)
