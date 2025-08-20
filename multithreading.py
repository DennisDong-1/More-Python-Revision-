#Multithreading allows you to run multiple threads (smaller units of a process) concurrently. In Python, due to the Global Interpreter Lock (GIL), threads are better suited for I/O-bound tasks rather than CPU-bound tasks.

# creating and starting threads

import threading
import time

def print_numbers():
    """Function to print numbers"""
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    """Function to print letters"""
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(1)

# Method 1: Using threading.Thread class
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Both threads have finished!")

# thread class inheritance

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay
    
    def run(self):
        """Method representing the thread's activity"""
        print(f"Thread {self.name} starting")
        self.count_down()
        print(f"Thread {self.name} finishing")
    
    def count_down(self):
        for i in range(5, 0, -1):
            print(f"Thread {self.name}: {i}")
            time.sleep(self.delay)

# Create and start threads
thread1 = MyThread("Thread-1", 1)
thread2 = MyThread("Thread-2", 0.5)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Main thread continuing execution")