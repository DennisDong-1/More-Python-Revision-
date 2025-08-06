""" First-Class Functions in Python
This example demonstrates how Python treats functions as first-class citizens.
That means functions can be passed as arguments, returned from other functions, and assigned to variables.
"""
# A Higher-Order Function that accepts another function as an argument
def calculation(func):
    # This is a wrapper function (a closure) that adds a layer around the original function
    def inner_function(x, y):
        return func(x, y)
    
    
    # Returns the wrapped version of the function
    return inner_function

# Function to add two numbers
def sum(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

#  Decorating functions manually by passing them into 'calculation'
s1 = calculation(sum)       # s1 becomes the wrapped version of sum
s2 = calculation(subtract)  # s2 becomes the wrapped version of subtract

# Call the wrapped functions and print results
print(s1(1, 2))   # Outputs: 3
print(s2(1, 7))   # Outputs: -6