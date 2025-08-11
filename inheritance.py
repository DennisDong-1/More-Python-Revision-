# Parent class
class Animal:
    def speak(self):
        print("This animal makes a sound")

# Child class inherits from Animal
class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

# Using inheritance
dog = Dog()
dog.speak()  # From Animal
dog.bark()   # From Dog

class Animal:
    def speak(self):
        print("This animal makes a sound")

class Cat(Animal):
    def speak(self):  # Overrides parent method
        print("Meow!")

cat = Cat()
cat.speak()
