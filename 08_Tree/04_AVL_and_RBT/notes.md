# AVL Trees and Red-Black Trees --- Notes

## AVL Tree

### Definition

An AVL tree is a self-balancing binary search tree where the height
difference between left and right subtrees is at most 1.

### Balance Factor

Balance Factor (BF) = height(left) -- height(right) Allowed values: -1,
0, +1

### Why AVL Trees?

-   Guarantees O(log n) search
-   Strictly balanced
-   Good for read-heavy operations

### Rotations

To maintain balance: - LL Case → Right Rotation - RR Case → Left
Rotation - LR Case → Left + Right Rotation - RL Case → Right + Left
Rotation

### Example (Insert 30, 20, 10)

Insertion leads to LL imbalance → Right rotation produces balanced tree.

### Use Cases

-   Databases
-   Search-intensive applications

------------------------------------------------------------------------

## Red-Black Tree

### Definition

A Red-Black Tree is a self-balancing BST with relaxed balancing using
coloring rules.

### Rules

1.  Every node is RED or BLACK.
2.  Root is always BLACK.
3.  NULL leaves are BLACK.
4.  No two RED nodes can be adjacent.
5.  Every path must have the same number of BLACK nodes (black-height).

### Why Red-Black Trees?

-   Fewer rotations than AVL
-   Faster insert/delete
-   Guaranteed O(log n) height
-   Widely used in real systems

### Fixing Imbalance

-   Recoloring (most common)
-   Rotations (left/right)

### Example (Insert 10, 20, 30)

RR imbalance → Left rotation + recolor produces a valid tree.

### Use Cases

-   Linux kernel scheduler
-   C++ STL map/set
-   Java TreeMap/TreeSet
-   File systems

------------------------------------------------------------------------

## AVL vs Red-Black (Quick Comparison)

  Feature              AVL                  Red-Black
  -------------------- -------------------- -------------------------
  Balance strictness   High                 Medium
  Rotations            More                 Fewer
  Search               Slightly faster      Slightly slower
  Insert/Delete        Slower               Faster
  Best for             Search-heavy tasks   System-level operations

