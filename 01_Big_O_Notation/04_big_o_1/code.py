# Python program to demonstrate O(1) time complexity

student_list = ["Alice", "Bob", "Charlie", "David", "Eva"]

def displayStudents(student_list):
    print(student_list[0]) # O(1) time complexity
    print(student_list[2]) # O(2) time complexity in general, but still considered O(1) for fixed index access

displayStudents(student_list)

