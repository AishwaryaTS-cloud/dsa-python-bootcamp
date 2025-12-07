# -------------------------
# Stack Implementation (using dynamic array)
# -------------------------

class Stack:
    def __init__(self):
        self.arr = []

    # Push -> add at last
    def push(self, value):
        self.arr.append(value)   # O(1) amortized

    # Pop -> remove last
    def pop(self):
        if not self.arr:
            raise IndexError("Stack is empty")
        return self.arr.pop()    # O(1)

    # Peek -> last element
    def peek(self):
        if not self.arr:
            raise IndexError("Stack is empty")
        return self.arr[-1]      # O(1)

    # Utility
    def is_empty(self):
        return len(self.arr) == 0


# -------------------------
# Queue Implementation (using Linked List)
# -------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None   # front
        self.tail = None   # rear

    # Enqueue -> add at end
    def enqueue(self, value):
        newNode = Node(value)

        if not self.head:
            self.head = newNode
            self.tail = newNode
            return

        self.tail.next = newNode
        self.tail = newNode      # O(1)

    # Dequeue -> remove from front
    def dequeue(self):
        if not self.head:
            raise IndexError("Queue is empty")

        value = self.head.value
        self.head = self.head.next   # O(1)

        if self.head is None:
            self.tail = None

        return value

    # Peek -> front element
    def peek(self):
        if not self.head:
            raise IndexError("Queue is empty")
        return self.head.value

    # Utility
    def is_empty(self):
        return self.head is None


# -------------------------
# Example Run
# -------------------------

if __name__ == "__main__":
    print("STACK DEMO")
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Top:", s.peek())
    print("Popped:", s.pop())
    print("New Top:", s.peek())

    print("\nQUEUE DEMO")
    q = Queue()
    q.enqueue(5)
    q.enqueue(10)
    q.enqueue(15)
    print("Front:", q.peek())
    print("Dequeued:", q.dequeue())
    print("New Front:", q.peek())

