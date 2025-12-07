"""
DSA Introduction – Time Complexity & Big-O Examples
"""

# ---------------------------------------------------------
# 1. O(1) — Constant Time
# ---------------------------------------------------------
def get_first_element(arr):
    # Accessing by index takes constant time
    return arr[0]


# ---------------------------------------------------------
# 2. O(n) — Linear Time
# ---------------------------------------------------------
def print_all_elements(arr):
    # Looping from start to end: cost grows with input size
    for item in arr:
        print(item)


# ---------------------------------------------------------
# 3. O(n²) — Quadratic Time
# ---------------------------------------------------------
def print_pairs(arr):
    # Two nested loops → n * n operations
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])


# ---------------------------------------------------------
# 4. O(log n) — Logarithmic Time
# ---------------------------------------------------------
def binary_search(arr, target):
    """
    Works only on sorted arrays.
    Cuts search space in half each step → log n.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# ---------------------------------------------------------
# 5. O(n log n) — Using Efficient Sorting Algorithms
# ---------------------------------------------------------
def sort_array(arr):
    # Python uses Timsort → O(n log n)
    return sorted(arr)


# ---------------------------------------------------------
# 6. Space Complexity Example
# ---------------------------------------------------------
def copy_array(arr):
    """
    Creates a new array of size n → O(n) extra space.
    """
    new_arr = []
    for item in arr:
        new_arr.append(item)
    return new_arr


# ---------------------------------------------------------
# 7. Multiple Approaches to the Same Task
#    Showing how readability & scalability differ.
# ---------------------------------------------------------

# Reverse a list — Method 1 (O(n))
def reverse_manual(arr):
    result = []
    for i in range(len(arr) - 1, -1, -1):
        result.append(arr[i])
    return result

# Reverse a list — Method 2 (O(n), but clearer)
def reverse_pythonic(arr):
    return arr[::-1]

# Reverse a list — Method 3 (O(n), using built-in)
def reverse_inbuilt(arr):
    arr.reverse()
    return arr


# ---------------------------------------------------------
# 8. Driver Code (for testing)
# ---------------------------------------------------------
if __name__ == "__main__":
    nums = [10, 20, 30, 40, 50]

    print("O(1): First element =", get_first_element(nums))

    print("O(n): Printing all elements")
    print_all_elements(nums)

    print("O(n²): Printing pairs")
    print_pairs([1, 2])

    print("O(log n): Binary Search for 30 =", binary_search(nums, 30))

    print("O(n log n): Sorted =", sort_array(nums[::-1]))

    print("O(n) Space: Copied array =", copy_array(nums))

    print("Reverse (manual):", reverse_manual(nums))
    print("Reverse (python slice):", reverse_pythonic(nums))
    print("Reverse (in-built):", reverse_inbuilt(nums))
# Note: In Python, list operations like insert and delete may have different performance
# characteristics due to dynamic resizing and memory management.
