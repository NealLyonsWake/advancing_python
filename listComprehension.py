"""
List comprehension exercises:
1. Write a Python program to check if the elements in list are unique or not. List: [1, 2, 3, 1 , 5, 80, 80, 90, 4, 5, 8, 9, 10]

2. Write a Python program to calculate the average of two lists: List A: [1, 10, 7, 3, 8], List B: [0, 9, 80, 4, 1]

3. Square the even numbers in mylist and store the result in a evenlist:  mylist = [2, 10, 5, 8, 7]
"""

"""
1.
"""
print("Exercise 1")
numbers = [1, 2, 3, 1, 5, 80, 80, 90, 4, 5, 8, 9, 10]

def unique_or_duplicate(numbers):
    unique_list = []
    duplicate_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
        else:
            duplicate_list.append(num)
    return (f'Unique numbers in the list are {unique_list}.\nDuplicate numbers are {duplicate_list}')

print(unique_or_duplicate(numbers))


"""
2.
"""
print("Exercise 2")
list_A = [1, 10, 7, 3, 8]
list_B = [0, 9, 80, 4, 1]


def average(a, b):
    return (sum(a) + sum(b)) / (len(a) + len(b))


print(average(list_A, list_B))


"""
3.
"""
print("Exercise 3")
mylist = [2, 10, 5, 8, 7]

def square_evens(mylist):
    evenlist = []
    for num in mylist:
        if num % 2 == 0:
            evenlist.append(num**2)
    return evenlist

print(square_evens(mylist))
