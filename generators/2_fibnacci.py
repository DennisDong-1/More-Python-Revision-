def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the generator
fib = fibonacci_generator()

for _ in range(10):
    print(next(fib))