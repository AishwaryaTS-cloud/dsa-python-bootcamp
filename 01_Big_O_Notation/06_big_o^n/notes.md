# **Notes: Understanding Quadratic Time — O(n²)**

In this lecture, the focus moves to **quadratic time**, also known as **O(n²)**.

You usually see this when your code has **a loop inside another loop** — a nested loop.

---

## **1. When Does O(n²) Happen?**

Quadratic time shows up when:

- You take each element from a list
- And for every element, you loop through the entire list again

Example meaning:

- Pick the 1st item → loop through the full list
- Pick the 2nd item → loop through the full list
- Pick the 3rd item → loop through the full list
- …and so on

If your list has **7 elements**:

- 1st element → 7 operations
- 2nd element → 7 operations
- 3rd element → 7 operations

Total = **7 × 7 = 49 operations** → that’s **n²**.

---

## **2. Visualizing the Work**

For a list of size `n`:

- Outer loop runs **n** times
- Inner loop runs **n** times
- Work done = **n × n = n²**

That’s why this pattern is called *quadratic time*.

---

## **3. Example Code**

```python
num_list = [1, 2, 3, 4, 5]

def randomFUnction(num_list):
    total = 0

    for num1 in num_list:          # O(n)
        for num2 in num_list:      # O(n)
            total += num1 + num2   # O(1)
    print("Total sum is:", total)
    return total

print("Final Sum:", randomFUnction(num_list))

```

---

## **4. Complexity Breakdown**

- Outer loop → **O(n)**
- Inner loop → **O(n)**
- Combined → **O(n × n) = O(n²)**
- Operation inside loop → **O(1)**
    
    but that doesn’t change the overall growth.
    

Final result:

### ✅ **O(n²)** — Quadratic time

---

## **5. When Inputs Differ (Rule: n × m)**

If the inner loop uses a different list, say:

- First list → size **n**
- Second list → size **m**

Then the total work becomes:

### **O(n × m)**

Example:

If one list has 7 elements and the other has 5, then:

7 (outer) × 5 (inner) = **35 operations**

This is still nested loops, but not square — it's multiplied by the size of two different inputs.

---

## **6. Key Takeaways**

- Nested loops that run fully → **O(n²)**
- Two different lists → **O(n × m)**
- Quadratic time grows *much* faster than linear time
- Even small lists can become expensive when squared

In the next lecture, simplification rules continue with rule number five.
