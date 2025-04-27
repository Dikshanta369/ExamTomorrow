# Simple Python program to find factorial of a number

# Function to find factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive call

# Example usage
num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")

