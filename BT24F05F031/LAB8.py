def add(a, b):
    return a + b

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Sum:", add(5, 3))
print("Factorial:", factorial(5))