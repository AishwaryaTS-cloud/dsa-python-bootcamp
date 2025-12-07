## **1. Stack — think of a pile of books**

A **stack** works on **LIFO** — *last in, first out*.

The last thing you put in is the only thing you can take out first. Imagine a pile of books: you can only remove the top one.

### **Key operations**

| Operation | Meaning | Time (Array) |
| --- | --- | --- |
| **push(x)** | Add to top | O(1) average |
| **pop()** | Remove top | O(1) |
| **peek() / top()** | Look at top | O(1) |

### **Why array works well for stacks**

Because all action happens at the **end** of the array:

- No shifting
- Just write or delete the last element
- So push/pop/peek are all O(1)

**Sources:** CLRS, Sedgewick Algorithms

---

## **2. Queue — think of a line at a movie theater**

A **queue** works on **FIFO** — *first in, first out*.

The first person who joins the line is the first person served.

### **Key operations**

| Operation | Meaning | Time (Array) | Time (Linked List) |
| --- | --- | --- | --- |
| **enqueue(x)** | Add to end | O(1) avg | O(1) |
| **dequeue()** | Remove from front | ❌ O(n) | ✅ O(1) |
| **peek()** | Front element | O(1) | O(1) |

### **Why array is bad for queues**

Removing the first element means shifting every element to the left:

```
[5, 6, 10, 9]  → dequeue 5
→ shift 6,10,9 → O(n)

```

That’s expensive.

### **Why linked list is perfect**

If you track **head** (front) and **tail** (back), then:

- dequeue = move head → O(1)
- enqueue = attach new node at tail → O(1)

**Sources:** CLRS, Sedgewick Algorithms, Stanford CS106B Notes

---

## **3. Summary: When to use what**

### **Use Stack when**

- Order matters as “reverse”
- Undo/redo
- Browser back button
- DFS
- Expression evaluation

### **Use Queue when**

- Order matters as “first come first serve”
- CPU scheduling
- BFS
- Handling requests in a pipeline

---

## **4. Time Complexity Recap**

### **Stack (array)**

- push → O(1)
- pop → O(1)
- peek → O(1)

### **Queue**

**Array implementation**

- enqueue → O(1)
- dequeue → O(n) ❌

**Linked list implementation**

- enqueue → O(1)
- dequeue → O(1) ✔️