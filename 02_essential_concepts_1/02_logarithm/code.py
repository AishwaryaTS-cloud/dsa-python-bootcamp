# Binary search to find the logarithm base 2 of a number

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Example
nums = [1, 3, 5, 7, 9]
print(binary_search(nums, 7))   # Output: 3
print(binary_search(nums, 4))   # Output: -1

# complexity analysis:
# The binary search algorithm divides the search space in half with each iteration.
# Therefore, the time complexity is O(log n), where n is the number of elements in the array.
# The space complexity is O(1) since it uses a constant amount of space.
# Logarithm function using recursion