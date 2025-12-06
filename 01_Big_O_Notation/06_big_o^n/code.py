num_list = [1, 2, 3, 4, 5]

def randomFUnction(num_list):
    total = 0

    for num1 in num_list:          # O(n)
        for num2 in num_list:      # O(n)
            total += num1 + num2   # O(1) per operation
    print("Total sum is:", total)
    return total
print("Final Sum:", randomFUnction(num_list))

# complexity analysis:
# O(n) * O(n) * O(1)
# = O(n^2) * O(1)
# = O(n^2)