# Depth, Height, and Edges in Trees — Notes

## 1. Depth of a Node

* Depth = number of edges from the **root** to that node.
* Root node always has depth **0**.
* Example:

  * Depth(9) → path: 3 → 5 → 9 → depth = 2 edges
  * Depth(5) → depth = 1
  * Depth(8) → depth = 2

## 2. Height of a Node

* Height = number of edges in the **longest path** from the node to a **leaf**.
* Example:

  * Height(5) → longest path from 5 to any leaf = 1 edge
  * Height(3) → if longest path is 3 → 5 → 9 → height = 2

### Important

* Depth is always measured **from the root downward**.
* Height is measured **from the node downward to leaves**, choosing the **longest** path.

## 3. Height of a Tree

* Defined as the **height of the root node**.
* Example:

  * If longest path from root has 3 edges → height of the tree = **3**.

## 4. Internal (Inner) Nodes

* Any node that is **not a leaf**.
* Examples:

  * If a node has at least one child → it’s an internal node.

## 5. Edges in a Tree

* Each node (except root) has exactly one incoming edge.
* **Formula:**

  * Number of edges = number of nodes − 1
* Example:

  * 7 nodes → 6 edges

## Quick Summary

* **Depth(node)** = distance from root → node
* **Height(node)** = longest distance from node → leaf
* **Height(tree)** = height of root
* **Internal nodes** = non-leaf nodes
* **Edges** = nodes − 1

