# Trees — Complete Notes

## 1. What Are Trees?

Trees are **non‑linear data structures** that store data in a hierarchical form. Unlike arrays, linked lists, stacks, or queues (which are linear), trees branch out.

A tree is made of **nodes** connected by **edges**, organized in levels.

---

## 2. Basic Terminology

### **Node**

A node is a single element of the tree. Every value you insert becomes a node.

### **Root**

The topmost node of the tree. It does not have a parent.

Example: In the sample tree, `3` is the root.

### **Parent**

A node that has one or more children.

### **Child**

A node that descends from a parent.

Example: For parent `3`, the children are `4` and `5`.

### **Leaf Node**

Nodes with **no children**.

Example: `6, 7, 8, 9`.

### **Siblings**

Nodes that share the same parent.

Examples: `(4, 5)`, `(6, 7)`, `(8, 9)`.

### **Edge**

A connection between two nodes.

Example: Edge between `3 → 4`.

### **Levels**

The height of a node within the tree.

* Level 0 → Root
* Level 1 → Children of root
* Level 2 → Grandchildren

### **Path**

Sequence of nodes you traverse.

Example: `3 → 5 → 9`.

### **Subtree**

A smaller tree inside the main tree.
Example: The tree rooted at `4` is a subtree.

---

## 3. Key Rules of Tree Structure

* A **parent can have many children**, but a **child has only one parent**.
* Direction is **top → bottom** (root to leaves).
* Every node can be: parent, child, both, or leaf.

Example: `4` is a child of `3`, but also a parent of `6` and `7`.

---

## 4. Real‑Life Examples of Trees

### **1. Facebook Comments**

* Your post = Root
* Comments = Children
* Replies = Child of that comment

### **2. HTML DOM Tree**

* `<html>` is the root
* `<head>` and `<body>` are children
* Inside `<body>` you have nested tags → subtree

### **3. Chess Move Computation**

Every move branches into multiple possible next moves.

### **4. Family Tree**

* Grandfather = Root
* Children = Next level
* You, siblings = Next level

---

## 5. Example Breakdown (Based on the Lecture)

Given this tree:

```
        3
      /   \
     4     5
   /  \   /  \
  6    7 8    9
```

### **Root:**

* 3

### **Parents:**

* 3, 4, 5

### **Children:**

* 4, 5, 6, 7, 8, 9

### **Leaf Nodes:**

* 6, 7, 8, 9

### **Siblings:**

* (4, 5)
* (6, 7)
* (8, 9)

### **Levels:**

* Level 0 → 3
* Level 1 → 4, 5
* Level 2 → 6, 7, 8, 9

### **Paths:**

* 3 → 4 → 6
* 3 → 4 → 7
* 3 → 5 → 8
* 3 → 5 → 9

### **Subtrees:**

* Subtree rooted at 4
* Subtree rooted at 5

---

## 6. Why Trees Matter in DSA

Trees unlock more advanced structures:

* Binary Trees
* Binary Search Trees (BST)
* AVL Trees
* Heaps
* Tries
* Segment Trees
* B‑Trees (used in databases)

They help with searching, indexing, organizing data, and solving recursive problems.

---
