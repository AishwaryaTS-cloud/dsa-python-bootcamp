# **Understanding Logarithms in Complexity Analysis**

## **1. What a Logarithm Really Means**

In computer science, when we say:

```
log N

```

we **always assume base 2** (unless stated otherwise).

A logarithm answers this question:

> How many times can I divide N by 2 until I reach 1?
> 

Mathematically:

```
log₂(x) = y
⇔
2ʸ = x

```

---

## **2. Basic Log Values (Base 2)**

| x | log₂(x) | Why |
| --- | --- | --- |
| 1 | 0 | 2⁰ = 1 |
| 2 | 1 | 2¹ = 2 |
| 4 | 2 | 2² = 4 |
| 8 | 3 | 2³ = 8 |
| 16 | 4 | 2⁴ = 16 |

Pattern you must remember:

> When you double N, log N increases by exactly 1.
> 

Example:

4 → 8 → 16

2 → 3 → 4

This slow growth is the reason log complexity is powerful.

---

## **3. Why Logs Matter in Complexity**

When input grows fast, log grows extremely slowly:

- log₂(8) = 3
- log₂(16) = 4
- log₂(1024) = 10
- log₂(1,000,000) ≈ 20

Even with *millions* of elements, log is still around **20**.

This makes **O(log N)** much better than **O(N)** for large data.

---

## **4. Where Logarithms Show Up in Algorithms**

You see log N complexity whenever an algorithm:

- keeps dividing the problem in half
- or eliminates half the data each step
- or splits the input repeatedly

Common examples:

- **Binary Search**
- **Merge Sort**
- **Quick Sort (average case)**
- **Heap operations**
- **Balanced binary trees**

---

## **5. Halving Example (Why Binary Search is Log N)**

Start with an array of 8 elements:

```
[0,1,2,3,4,5,6,7]

```

Each step eliminates half:

1. 8 → 4
2. 4 → 2
3. 2 → 1

Steps = **3**

And:

```
log₂(8) = 3

```

Same logic for 16 elements:

16 → 8 → 4 → 2 → 1

Steps = 4

log₂(16) = 4

---

## **6. Splitting Example (Sorting)**

If an algorithm keeps dividing input:

16 → 8 → 4 → 2 → 1

Steps again = **log₂(16) = 4**

This is why sorting algorithms often have **N log N** complexity:

- N work at each level
- log N levels

---

## **7. Approximations in Logarithms**

Inputs won’t always be exact powers of 2.

For example:

- N = 30
- Closest power of 2 is 32
- log₂(32) = 5

We approximate because it keeps reasoning simple.

Big-O is about *trend*, not exact numbers.

---

## **8. Key Takeaways**

- In CS, logs are **always base 2 by default**.
- Doubling N → log increases by only **1**.
- log grows *very* slowly, so **O(log N)** is extremely efficient.
- You’ll see logs everywhere in searching and sorting.
- Any algorithm that halves the input repeatedly = **O(log N)**.

