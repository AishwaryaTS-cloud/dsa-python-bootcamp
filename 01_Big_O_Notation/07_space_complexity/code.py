def display_cube(n):
    """Display the cube of each number from 1 to n.

    This function uses O(1) space complexity since it only uses a fixed amount
    of additional space regardless of the input size n.

    Args:
        n (int): The upper limit of numbers to display cubes for.
    """
    for i in range(1, n + 1):
        print(f"The cube of {i} is {i ** 3}")

# Example usage
display_cube(5)
# complexity analysis:
# The function uses a loop that runs n times, but it does not use any additional
# data structures that grow with n. Therefore, the space complexity is O(1).
