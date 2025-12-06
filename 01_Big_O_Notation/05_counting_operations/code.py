students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ian", "Jack"]

def randomFunction(student_list):
    first = students[0]          # O(1)
    second = students[1]         # O(1)

    total = 0                    # O(1)
    new_list = []                # O(1)

    for student in student_list:  # O(n)
        new_list.append(student)  # O(1) per operation
        total += 1                # O(1) per operation
    print("Total students processed:", total)

    print(new_list)
    return total

print("Final Count:", randomFunction(students))

# complexity analysis:
# O(1) + O(1) + O(1) + O(1) + O(n) * (O(1) + O(1))
# = 4O(1) + O(n) * 2O(1)
# = O(1) + O(n)
# = O(n)