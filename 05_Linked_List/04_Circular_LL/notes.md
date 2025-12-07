# Circular & Basic Linked List Implementation — Notes

## 1. Circular Linked List

A circular linked list is just like a singly linked list with one difference:

* The **last node does not point to None**.
* Instead, it points back to the **head**.

Example:

```
3 -> 7 -> 2 -> 9
^              |
|______________|
```

Traversal keeps going in a loop:

* 3 → 7 → 2 → 9 → 3 → …

This structure is useful in situations where you want endless cycling, like round-robin.

---

## 2. Building a Linked List (Basic Idea)

To build any linked list, you do two things:

1. **Create nodes** using a Node class.
2. **Connect nodes** using pointers.

### Node Structure (Singly)

Each node stores:

* `value`
* `next`

By default, `next = None`.

### Example Nodes

```
n1(value=3)
n2(value=7)
n3(value=2)
n4(value=9)
```

### Connecting Nodes

```
n1.next = n2
n2.next = n3
n3.next = n4
```

### Linked List Class

A linked list class holds:

* `head` pointer
* methods such as insert, delete, search, traverse

Initial state:

```
head = None
```

Then we attach:

```
head = n1
```

This gives us a working linked list.

---

## 3. Why Use Classes?

Classes help you:

* create reusable node objects
* store head
* organize operations (insert, delete, search)

Without classes you would manually connect nodes every time, which is not scalable.

---

## 4. Methods You Typically Implement

Inside the LinkedList class:

* `insert(value)`
* `delete(value)`
* `search(value)`
* `traverse()`
* `get(index)`

These operations hide the pointer-handling from the user.

---

## 5. Doubly Linked List Structure

Adds one more pointer:

* `prev`
* `data`
* `next`

```
self.prev = None
self.data = value
self.next = None
```

During connection:

```
node.next = next_node
next_node.prev = node
```

This allows movement in both directions.

---

These concepts form the base before moving to interview-style implementations like "Design Linked List".
