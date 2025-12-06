student_list1 = ["Alice", "Bob", "Charlie", "David", "Eva"]
student_list2 = ["Frank", "Grace", "Hannah", "Ian", "Jack"]

def checkStudentInList(student_list):
    for student in student_list:
        if student == "Charlie":
            print("Available")
    else:
        print("Not Available")

checkStudentInList(student_list1)
checkStudentInList(student_list2)

# Python program to demonstrate O(n) time complexity

