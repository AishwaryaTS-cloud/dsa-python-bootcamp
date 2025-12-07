# Hashing & Hash Tables — Notes

## 1. What is Hashing?

Hashing is a technique used to map data to a fixed-size value called a *hash*. This mapped value determines where the data will be stored inside a hash table.

In simple terms: **hashing = converting a key into an index**.

---

## 2. Hash Table

A hash table is a data structure that stores key–value pairs. It uses a hash function to compute an index for each key. Ideally, different keys map to different indexes.

**Average time complexity:**

* Search → O(1)
* Insert → O(1)
* Delete → O(1)

Worst case for all operations → O(n), usually caused by collisions.

---

## 3. Hash Function

A hash function takes a key and returns an integer index within the table’s size.

A good hash function:

* Spreads keys uniformly
* Is fast to compute
* Minimizes collisions

**Common examples:**

* `h(key) = key % table_size`
* Folding method
* Mid-square method
* String hashing (e.g., polynomial rolling hash)

---

## 4. Collisions

A collision occurs when two different keys map to the same index.

**Why collisions happen:**

* Limited table size
* Imperfect hash function

Collisions are unavoidable, so we need ways to handle them.

---

## 5. Collision Handling Methods

### **A. Open Addressing**

All elements are stored directly within the table.

1. **Linear Probing**

   * If index `i` is full, try `i+1`, `i+2`, ...
   * Simple but can cause clustering.

2. **Quadratic Probing**

   * Try `i+1^2`, `i+2^2`, `i+3^2`...
   * Reduces clustering.

3. **Double Hashing**

   * Use a second hash function to compute step size.
   * Very effective at spreading keys.

---

### **B. Separate Chaining**

Each index of the table stores a linked list.
If multiple keys hash to the same index, they are appended to the list.

Pros:

* Easy to implement
* Works well even when table load is high

Cons:

* Needs extra memory for pointers

---

## 6. Load Factor (α)

```
α = number_of_elements / table_size
```

It tells how full the hash table is.

For open addressing, performance drops drastically when α > 0.7.

Hash tables typically resize when load factor crosses a threshold.

---

## 7. Rehashing

When the table gets too full or performance drops, the table is resized (often doubled), and all keys are reinserted using the hash function.

---

## 8. Applications of Hash Tables

* Databases and indexing
* Caches (e.g., LRU cache)
* Symbol tables in compilers
* Implementing sets & dictionaries
* Password storage (with cryptographic hashing)

---

## 9. Summary

* Hashing maps keys to indexes.
* Hash tables give O(1) operations on average.
* Collisions are handled using chaining or open addressing.
* Load factor and rehashing maintain performance.

---