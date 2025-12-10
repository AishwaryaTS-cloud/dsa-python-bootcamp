# Heap Sort & Priority Queue — Notes

## 1. What is Heap Sort?
Heap sort is a sorting algorithm that uses a **Max Heap** or **Min Heap** to arrange elements in sorted order.
- If we use a **Max Heap**, we get the sorted output in **ascending** order.
- If we use a **Min Heap**, we get the sorted output in **descending** order.

---
## 2. Core Idea of Heap Sort
1. Build a heap from the given array.
2. Remove the root element (max in Max Heap) — this is the largest value.
3. Place that removed value at the end of the array.
4. Restore (heapify) the heap.
5. Repeat for all remaining elements.

Each removal sorts **one element**, so in the end the array becomes sorted.

---
## 3. Example Flow (Max Heap → Ascending Sort)
Given elements: `80, 73, 69, 56, 52, 51, 45`

During heap sort:
- Remove 80 → placed at last
- Remove 73 → next position
- Remove 69 → next
- … and so on

Final sorted list (ascending):  
`45, 51, 52, 56, 69, 73, 80`

---
## 4. Time Complexity
| Operation | Complexity |
|----------|------------|
| Building heap | **O(n)** |
| Removing each element | **O(log n)** |
| Total (n removals × log n)** | **O(n log n)** |

---
## 5. Visualising Insertion (Building Heap)
Insert elements one by one:
- Add at next open leaf
- Compare with parent
- Swap if needed (heapify up)

Example sequence inserted:  
`73 → 56 → 80 → 69 → 45 → 51 → 52`

Heap formed by maintaining max-heap rules.

---
## 6. Visualising Deletion (Heap Sort)
When deleting from Max Heap:
1. swap root ↔ last element  
2. remove last element (max value)  
3. heapify down from root

Repeat until all elements are removed and placed into sorted order.

---
## 7. What is a Priority Queue?
A **Priority Queue** is like a queue, but items are served based on priority.
- Highest priority = highest value (in a Max Heap)
- Or smallest value if using Min Heap

Real-life idea: VIPs go first, then online bookings, then regular line.

---
## 8. Problems With Normal Queue (When Priority Needed)
If we use a simple queue:
- **Insertion:** O(1)  
- **Finding highest priority:** O(n)  
- **Deleting highest priority:** O(n) because shifting elements

Total deletion cost becomes inefficient.

---
## 9. Why Heap Is Better for Priority Queue
Using a heap to store priorities gives:
- **Insertion:** O(log n)
- **Delete highest priority:** O(log n)

Much faster than O(n) for deletion in normal queue.

---
## 10. Summary
- Heap sort removes one element at a time from a max heap to produce ascending order.
- Each deletion gives the next largest element.
- Priority queue uses heap so highest-priority elements are always extracted efficiently.
- Heap operations stay within **O(log n)**, making them suitable when priority-based processing is required.

