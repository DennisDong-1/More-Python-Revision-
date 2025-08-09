# Zip -> a built in function that aggregates elements from multiple iterables and returns an iterator of tuples

# syntax - zip(*iterables), takes multiple iterables as input, pairs each element from each iterable based on their position
# used when you need to process multiple sequence in paralles, need to combine data from diff sources

# iter1 = [1, 2, 3, 4, 5]
# iter2 = [10, 20, 30, 40, 50]
# iter3 = [100, 200, 300, 400]

# z1 = zip(iter1, iter2, iter3)
# print(z1)

# print(list(z1))

# print(next(z1))
# print(next(z1))
# print(next(z1))
# print(next(z1))
# print(next(z1))

# Common use cases

product = ["Towels", "Pants", "Socks"]
price = [100, 50, 20]

# for prd, pr in zip(product, price): # parallel iteration
#     print(f"{prd}: ${pr}")

# product_dict = dict(zip(product, price)) # creating dictionaries
# print(product_dict)

# unzip using * operator

# zipped = zip(product, price)

# p, price = zip(*zipped)
# print(p)
# print(price)

# transposing data(matrix transformation)

# matrix = [[1, 2, 3], [10, 20, 30]]

# print(list(zip(*matrix)))

# zip_longest() -> handles unequal length iterables, fills missing values with a specified fillvalue(default = None)

from itertools import zip_longest

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [123]

print(list(zip_longest(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue="---")))