# array_common_operations
# Demonstration of common array operations and their time complexities

# In Python, lists behave like dynamic arrays
# but the conceptual time complexities remain similar.

# 1. Accessing an element (O(1))
arr = [10, 20, 30, 40, 50]
index = 2
value = arr[index]  # constant time access
print("Access:", value)

# 2. Updating an element (O(1))
arr[index] = 99
print("Update:", arr)

# 3. Traversing the entire array (O(n))
print("Traverse:")
for element in arr:
    print(element)

# 4. Searching an element (O(n))
target = 40
found = False
for element in arr:
    if element == target:
        found = True
        break
print("Search result:", found)

# 5. Insertion (O(n) due to shifting in static arrays)
# Python list handles resizing internally, but conceptually it's still linear.
arr.insert(2, 77)
print("Insert:", arr)

# 6. Deletion (O(n))
arr.pop(3)
print("Delete:", arr)
