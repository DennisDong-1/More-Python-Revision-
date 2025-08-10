# lets a class call methods from its parent (or sibling classes) without hardcoding the parent's name

class Animal: # Basic example
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()  # calls Animal.speak()
        print("Woof!")

d = Dog()
d.speak()

# In multiple inheritance

class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        super().greet()
        print("Hello from B")

class C(A):
    def greet(self):
        super().greet()
        print("Hello from C")

class D(B, C):
    def greet(self):
        super().greet()
        print("Hello from D")

print(D.mro())  # Shows the resolution order
D().greet()
