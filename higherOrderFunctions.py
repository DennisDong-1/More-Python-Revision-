# Higher order functions - Functions that either:
                    # Take one or more functions as arguments or
                    # Return a function as their result
# Python supports them and treats functions as first-class objects, meaning they can be passed around and used as arguments just like any other object

# built-in hof -> map, filter, sorted

import math

# Maps -> built-in hof that applies a given function to each item of an iterable and returns an iterator(map object) with results

# map(function, iterable, ...)

# def sigmoid(x : float) -> float :
#     return 1/(1 + pow(math.e, -x))

# l1 = [1, 2, 3]

# print(map(sigmoid, l1))
# print(next(result))

# def square_fun(x : int) -> int :
#     return x**2

# l1 = [1, 2, 3, 4, 5]

# print(list(map(square_fun, l1)))

# def formula1( a, b : int ) -> int : 
#     return (a + b)**2

# l2 = [1, 2, 3]
# l3 = [1, 2, 3]
# print(list(map(formula1, l2, l3)))

# l1 = [1,2,3]
# l2 = [4,5,6]

# print(list(map(lambda x, y: x + y, l1, l2)))

# words = ["Fascinating", "Beauty", "Wisdom"]

# print(list(map(len, words)))

# |||||||||||||||||||||||||||||||||||||||||||||||||||

# Filter -> hof that constructs an iterator from elements of an iterable for which a function returns true

# l2 = [1, 2, 3, 4, 5, 6, 7, 8]

# def filter1(x):
#     return x %2 == 0

# l1 = [i for i in range(1, 25)]

# result = list(filter(filter1, l1))

# print(result)

# print(list(filter(lambda x: x %2 != 0, l1)))

# user_db = ["a@gmail.com", "b@gmail.com", "c@gmail.com", "x@gmail.com", "y@gmail.com", "z@gmail.com"]
# subs = {"a@gmail.com": 1,
#         "b@gmail.com": 0,
#         "c@gmail.com": 0,
#         "x@gmail.com": 0,
#         "y@gmail.com": 0,
#         "z@gmail.com": 1,
#         }

# def check(email):
#     # return subs.get(email, 0) == 1

#     if subs.get(email, 0) == 1:
#         return True
#     return False

# print(list(filter(check, user_db)))

# Filtering students who passed (less than 50 = Fail)

# grades = {
#     "John": 45,
#     "Jane": 82,
#     "Tom": 60,
#     "Alice": 39
# }

# def check_grade(grade):
#     # if grades.get(grade) < 50:
#     #     return True
#     # return False

#     return grades.get(grade) < 50

# print(list(filter(check_grade, grades)))

# Filter numbers divisible by both 2 and 3

# nums = list(range(1, 31))

# def check_divisibility(n):
#     return n %2 == 0 and n %3 == 0

# print(list(filter(check_divisibility, nums)))

# emails = ["a@gmail.com", "b@gmail.com", "c@gmail.com"]
# status = {"a@gmail.com": "active", "b@gmail.com": "inactive", "c@gmail.com": "active"}

# print(list(filter(lambda email: status.get(email) == "active", emails)))

# Filter users with even ages

users = [
    {"name": "Alice", "age": 22},
    {"name": "Bob", "age": 35},
    {"name": "Charlie", "age": 28}
]

def check(user):
    if user["age"] %2 == 0:
        return True
    return False

print(list(filter(check, users)))
print(list(filter(lambda u: u["age"] %2 == 0, users)))