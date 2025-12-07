# Doubly Linked List — Notes

## Structure

A doubly linked list node stores three pieces of information:

* **data** (value)
* **prev** (pointer to previous node)
* **next** (pointer to next node)

If each pointer/data occupies 4 slots:

* prev → 4
* data → 4
* next → 4

Total per node = **12 slots**.

This uses more memory than singly linked list, but gives extra flexibility.

---

## Basic Layout Example

```
None <- [3] <-> [7] <-> [2] <-> [9] -> None
```

Every node knows both its neighbors.

---

## Traversal

### Forward traversal

Start from head and follow `next` pointers.

### Backward traversal

Start from tail and follow `prev` pointers.

Because each node has `prev`, you can move backwards without extra storage.

---

## Insertion

Insertion logic is similar to singly linked list, but with one extra update:

### Insert at beginning

Steps:

1. Create new node.
2. new.prev = None
3. new.next = old_head
4. old_head.prev = new
5. head = new

### Insert at end

Steps:

1. Create node
2. new.next = None
3. new.prev = old_tail
4. old_tail.next = new
5. tail = new

### Insert in middle

For node A → B, and we insert X between them:

1. X.prev = A
2. X.next = B
3. A.next = X
4. B.prev = X

Complexity remains **O(1)** if you already have the node.
If you must search → **O(n)**.

---

## Deletion

Deletion requires updating **both next and prev** pointers.

### Delete a middle node B

Given A <-> B <-> C:

1. A.next = C
2. C.prev = A
3. B becomes unreachable

### Delete head

1. head = head.next
2. head.prev = None

### Delete tail

1. tail = tail.prev
2. tail.next = None

Complexity:

* **O(1)** if node is given
* **O(n)** if search is needed

---

## Key Advantage

You can move in both directions

* forward
* backward

This makes some operations easier (like reverse traversals), at the cost of extra memory.

---

These concepts map directly to the code implementation.
