# **Understanding Big O(1) — Constant Time Complexity**

## **1. What Big O(1) Really Means**

- Big O(1) represents **constant time**.
- The number of operations does *not* change based on how large the input is.
- Whether the input list has 3 items, 9 items, or 100 items — the code performs the **same number of operations**.

---

## **2. Example: Accessing the First Element**

```python
students = ["Andrew", "Sam", "John", ...]
print(students[0])

```

### Why is this O(1)?

- You always print the **first element**.
- No looping. No scanning through the list.
- Input size doesn’t matter — the task is fixed.
- So it always takes **one operation**.

---

## **3. Visualizing It on a Graph**

- Input size: 1 → operations: 1
- Input size: 5 → operations: 1
- Input size: 9 → operations: 1

The graph is a **flat horizontal line** — no growth as input grows.

---

## **4. What If We Do Two Operations?**

Example:

```python
print(students[0])
print(students[1])

```

- Still constant time.
- Even though it’s *two* operations, the number doesn’t grow with input size.
- Whether the list has 2 items or 200 items — you still perform **exactly 2 operations**.

This is why in Big-O notation:

- **O(2)**
- **O(5)**
- **O(10)**
    
    …all simplify to **O(1)**.
    

We only care about *growth*, not exact counts.

If you're looking for the actual implementation, go to `code.py` for the proper code.

---

## **5. When Do We Use Big O(1)?**

Any operation that does **not** scale with input size:

- Accessing an element by index
- Updating a value in a fixed position
- Simple arithmetic operations
- Returning a constant result

---

## **6. Summary**

- Big O(1) = constant time
- Operations don’t change as input grows
- O(2), O(5), O(10)… → all simplify to **O(1)**
- Accessing or printing fixed positions in a list is the classic example

This is one of the simplest and most efficient complexities you’ll encounter.