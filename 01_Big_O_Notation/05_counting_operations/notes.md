# Counting Operations & Building Big-O Step by Step

This lecture moves from understanding constant and linear time to **counting operations line by line**. The aim is to see how each statement contributes to overall complexity.

---

## 1. Start With Only Two Options

So far we only use:

- **O(1)** → constant time
- **O(n)** → linear time

Every line you analyze will fall into one of these categories.

---

## 2. The Example Code

```python
students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ian", "Jack"]

def randomFunction(student_list):
    first = students[0]          # O(1)
    second = students[1]         # O(1)

    total = 0                    # O(1)
    new_list = []                # O(1)

    for student in student_list:  # O(n)
        new_list.append(student)  # O(1) per operation
        total += 1                # O(1) per operation
    print("Total students processed:", total)

    print(new_list)
    return total

print("Final Count:", randomFunction(students))

```

> For the actual file, see code.py.
> 

---

## 3. Breaking Down the Code (Line-by-Line)

**Assignments and initializations** (run once):

- `first = students[0]` → **O(1)**
- `second = students[1]` → **O(1)**
- `total = 0` → **O(1)**
- `new_list = []` → **O(1)**

Everything above runs exactly once regardless of input size.

**Loop section**:

```python
for student in student_list:  # O(n)
    new_list.append(student)  # O(1)
    total += 1                # O(1)

```

- The loop body executes once for every element in `student_list` → **O(n)**.
- Each operation inside the loop is O(1), but repeated n times.

**Final prints / return**:

- `print("Total students processed:", total)` → **O(1)**
- `print(new_list)` → **O(1)**
- `return total` → **O(1)**

---

## 4. Combine the Counts

Raw breakdown:

```
O(1) + O(1) + O(1) + O(1) + O(n) * (O(1) + O(1)) + O(1) + O(1) + O(1)

```

Simplify constants and group terms:

```
4 * O(1) + O(n) * 2 * O(1) + 3 * O(1)
= O(1) + O(n)

```

So the final complexity is:

### ✅ **O(n)** — linear time

---

## 5. Key Takeaways

- Lines that run once: **O(1)**
- Code inside loops: **O(n)** (because it repeats for each input item)
- When you sum everything and simplify, the term that grows with input size dominates — here, **O(n)**.
- Counting operations first (raw form) then simplifying is the reliable way to determine Big-O.

---

## 6. Where to find the code

For the proper implementation, examples, and to run this yourself, open:

**`code.py`**

