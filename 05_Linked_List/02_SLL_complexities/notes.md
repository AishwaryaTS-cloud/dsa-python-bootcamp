# Linked List Complexities — Notes

## 1. Access (Getting an element by position)

* A linked list doesn’t store elements in contiguous memory.
* You only know the address of the **head**.
* To reach any position, you must start at the head and follow `next` pointers.
* Even if you want the 3rd or the last element, you have to walk through the earlier ones.

**Time Complexity:** **O(n)**

Reason: You may have to visit every node before reaching the target.

---

## 2. Search (Finding a value)

* Same story as access.
* You check each node one by one.
* Worst case: the element is at the end (or doesn’t exist).

**Time Complexity:** **O(n)**

---

## 3. Insertion

There are three cases:

### a. Insert at the start

Steps:

1. Create a new node.
2. Set its `next` to the current head.
3. Update `head` to this new node.

**If head is known:** **O(1)**

---

### b. Insert at the end

Two possibilities:

* **If `tail` is known:**

  * Create a node.
  * Set `tail.next` to this node.
  * Update `tail`.
  * **O(1)**

* **If `tail` is NOT known:**

  * Traverse from head to last node.
  * Then insert.
  * **O(n)**

---

### c. Insert in the middle (after any known node)

Steps:

1. Create a new node.
2. Set newNode.next = current.next
3. Update current.next = newNode

**If you already have the node:** **O(1)**

**If you must first search for that node:** **O(n)**

---

## 4. Deletion

Again, three cases:

### a. Delete at the start

* Move `head` to `head.next`.
* Old node gets garbage collected.

**O(1)**

---

### b. Delete at the end

* **If you know the previous node:**

  * Set previous.next = None
  * Update tail
  * **O(1)**

* **If you don’t know the previous node:**

  * Traverse the entire list to reach it
  * **O(n)**

---

### c. Delete in the middle

Steps:

1. Suppose you want to delete node B and you have pointer to A (previous).
2. Set A.next = B.next
3. B becomes unreachable.

**If you have pointer to previous node:** **O(1)**

**If you need to find that previous node:** **O(n)**

---

## Summary Table

| Operation                     | Best Case | Worst Case |
| ----------------------------- | --------- | ---------- |
| Access                        | O(n)      | O(n)       |
| Search                        | O(n)      | O(n)       |
| Insert (start)                | O(1)      | O(1)       |
| Insert (end, tail known)      | O(1)      | O(1)       |
| Insert (end, tail unknown)    | O(n)      | O(n)       |
| Insert (middle, node known)   | O(1)      | O(1)       |
| Insert (middle, node unknown) | O(n)      | O(n)       |
| Delete (start)                | O(1)      | O(1)       |
| Delete (end, prev known)      | O(1)      | O(1)       |
| Delete (end, prev unknown)    | O(n)      | O(n)       |
| Delete (middle, prev known)   | O(1)      | O(1)       |
| Delete (middle, prev unknown) | O(n)      | O(n)       |

---

These are the core complexities you need to remember for singly linked lists. Next step: doubly linked lists.
