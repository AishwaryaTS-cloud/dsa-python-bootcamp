# **Arrays in Python — Notes**

## **1. Introduction to Arrays**

In Python, you mainly work with two types of "array-like" structures:

1. **Python List** (built-in, flexible, dynamic)
2. **`array` Module Array** (typed, memory-efficient, C-style)

Both serve different purposes depending on flexibility, memory efficiency, and performance needs.

---

## **2. Python List**

A Python list is a **dynamic array of pointers**. It does not store actual values directly.

### **How a List Stores Data**

* Each element in the list is a **pointer/reference** to an object in memory.
* The actual data (like integers) lives separately in the heap.
* The list itself stores:

  * A pointer array (slots)
  * Current size
  * Allocated capacity (extra space for growth)

### **Memory Behavior of Python List**

* Python over-allocates memory for faster append operations.
* When space runs out, it resizes by allocating a bigger block.
* Since elements are pointers, lists can store mixed data types.

### **Pros**

* Dynamic resizing
* Flexible (can store any type)
* Fast indexing

### **Cons**

* High memory usage (each element = pointer + object overhead)
* Not contiguous like low-level arrays

---

## **3. Python `array` Module**

The `array` module provides a **typed, compact, contiguous array** similar to C arrays.

### **How `array` Stores Data**

* Stores actual values directly, not pointers.
* All elements must be the **same type**.
* Type is declared using a typecode (e.g., `'i'` for int, `'f'` for float).

### **Memory Behavior of `array` Module**

* Stores values in continuous memory blocks.
* Much more memory-efficient than lists.
* Suitable for large numerical datasets.

### **Pros**

* Low memory usage
* Contiguous layout (like C arrays)
* Faster for numeric workloads

### **Cons**

* Only one data type allowed
* Less flexible than lists

---

## **4. Static vs Dynamic Nature**

### **Static Arrays (like in C)**

* Fixed size
* Stored contiguously
* Very memory-efficient
* No resizing allowed

### **Dynamic Arrays (Python List)**

* Can grow or shrink
* Uses pointer array + over-allocation strategy
* Elements may scatter in memory

### **Python `array` Module — Hybrid**

* Still dynamic (it can resize)
* But data is contiguous and type-restricted

---

## **5. Memory Comparison Overview**

| Feature           | Python List    | Python `array` | C Array       |
| ----------------- | -------------- | -------------- | ------------- |
| Stores            | Pointers       | Actual values  | Actual values |
| Memory            | High           | Low            | Very low      |
| Type              | Mixed          | Single type    | Single type   |
| Layout            | Non-contiguous | Contiguous     | Contiguous    |
| Speed for numbers | Medium         | High           | Very high     |

---

## **6. Key Takeaways**

* Python lists are **flexible but memory-heavy** because they store references.
* Python's `array` module is **more memory-efficient** and closer to C arrays.
* If you want true low-level speed and memory efficiency, use:

  * `array` module for Python
  * or NumPy for numerical computing
* Python trades memory for flexibility and ease of development.

---

---

## **7. Dynamic Behavior Examples

Below examples show that Python arrays (from the `array` module) can grow, shrink, and modify size, which confirms they are dynamic.

### **Example 1 — Append (grows)

```python
from array import array

a = array('i', [10, 20, 30])
a.append(40)
print(a)  # array('i', [10, 20, 30, 40])
```

### **Example 2 — Pop (shrinks)

```python
a.pop()
print(a)  # array('i', [10, 20, 30])
```

### **Example 3 — Insert (modifies structure)

```python
a.insert(1, 99)
print(a)  # array('i', [10, 99, 20, 30])
```

### **Conclusion**

These operations show that the array size is not fixed and can change during runtime — a clear sign of a **dynamic array**.

---
