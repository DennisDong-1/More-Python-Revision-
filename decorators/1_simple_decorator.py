

def calculation(somefunction):
    # This is a wrapper function that adds behavior before calling the original function
    def inner_function(x, y):
        print("Some random calculations...")  # Additional behavior before the actual function call
        return somefunction(x, y)             # Calls the original function with provided arguments
    
    # Returns the wrapped version of the original function
    return inner_function

# Applying the decorator to the function using '@' syntax
@calculation
def sum(a, b):
    # Function to add two numbers
    return a + b

# Call the decorated function and print the result
print(sum(5, 6))  
