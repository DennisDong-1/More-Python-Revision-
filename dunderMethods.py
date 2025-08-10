# special methods that start and end with __ (two underscores), allows your object to behave like built-in types and hook into Python's syntax

class Greeter: # Basic example
    def __call__(self, name):
        print(f"Hello {name}!")

g = Greeter()
g("Alice")  # works like a function call

# Example of combining dunder methods

class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(5, 7)
print(v1 + v2)  # Vector(7, 10)
