# Python program to find the time complexity of a function
import time 
time.time()

timestamp_start = time.time()

# Python progrma to find sum of first n natural numbers

def sum_natural_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

n = 10
print ("Sum of first", n, "natural numbers is:", sum_natural_numbers(n))

# Program COmpleted

timestamp_end = time.time()
print("Time taken to execute the program:", timestamp_end - timestamp_start, "seconds")