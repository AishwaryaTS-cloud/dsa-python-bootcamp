# Notes: Introduction to Linked Lists (DSA)

## 1. What a Linked List Really Is

A linked list is a data structure made of **nodes**, where each node stores:

- a value
- a pointer/reference to the next node

Unlike arrays, the elements of a linked list **don’t sit next to each other in memory**.

They are scattered, but linked together using pointers.

---

## 2. Why Do We Even Need Linked Lists?

Arrays have one problem:

They demand **continuous memory**.

If a big block of memory isn’t free, the array can’t grow — even if memory is available in smaller fragmented pieces.

Linked lists solve this:

- Nodes can be stored **anywhere** in memory.
- Each node just needs to know **where the next one is**.

So linked lists are flexible with memory.

---

## 3. How a Node Looks Internally

Each node has two parts:

```
[data | next]

```

- **data** → the value (3, 7, "hello", etc.)
- **next** → address/reference of the next node

The chain ends when `next = None`.

---

## 4. Comparing Arrays vs Linked Lists (Memory Level)

### **Arrays**

- Stored in a single continuous block.
- Great for indexing:
    
    **address = base + index × size**
    
- But resizing is costly and needs big empty space.

### **Linked Lists**

- Nodes can be placed anywhere.
- Each node uses extra memory for the pointer.
- Slower indexing because you must move step by step.

---

## 5. Types of Linked Lists

### **a. Singly Linked List**

Each node points only to the next one.

```
3 → 7 → 2 → 9 → None

```

Traversal moves **forward only**.

---

### **b. Doubly Linked List**

Each node knows:

- previous node
- next node

```
None ← 3 ↔ 7 ↔ 2 ↔ 9 → None

```

You can move **both directions**, which makes some operations faster.

---

## 6. How Traversal Works

You start from the **head** and follow the `next` pointers:

```
head → head.next → head.next.next → ...

```

You can’t skip steps (unlike arrays where `arr[1000]` is instant).

---

## 7. The Big Picture

Linked lists give you:

- **Easy insertion and deletion**
- **Flexible memory usage**
- **No need for continuous memory blocks**

But at the cost of:

- Extra pointer memory
- No direct indexing
- Slower searches