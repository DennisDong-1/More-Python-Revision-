# Lambda functions - Small, anonymous functions, used for short, simple operations
# Syntax -> lambda arguments: arguments
# Can have multiple arguments, but only one expression, result is automatically returned

# cubes = lambda x: x**3
# print(cubes(3))

# sum = lambda a,b,c : a+b+c
# print(sum(10,20,30))

# students = {"name": "Dennis", "age": 23}, {"name": "Likhil", "age": 22}, {"name":"Pratik", "age": 21}

# sort_using_asc_age = sorted(students, key = lambda i: i["age"])
# print(sort_using_asc_age)

# Using in map

nums = [123, 456]

print(list(map(lambda x: x * 123, nums)))