print("This is Bug Hunter Practically!")
print("Testing will help me find bugs that users might encounter")

class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        # Fix the multiply bug here - remove the 0.01 addition for float multiplication
        return a * b
    def divide(self, a, b):
        # Fix the division bug here - raise an exception instead of returning a string
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    def power(self, a, b):
        # Fix the power function here
        # Hint: how should negative exponents be handled?
        if b < 0:
            return 1 / (a ** abs(b))
        return a ** b
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def fibonacci(self, n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

class PreciseCalculator(Calculator):
    def __init__(self, precision=2):
        super().__init__()
        self.precision = precision

    def add(self, a, b):
        result = super().add(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

