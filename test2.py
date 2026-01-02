
# Function to generate Fibonacci series
def fibonacci(n):
    # Initialize first two numbers
    a, b = 0, 1
    # Print first number
    print(a, end=' ')
    
    # Generate fibonacci numbers
    for i in range(n-1):
        print(b, end=' ')
        # Calculate next number by adding previous two
        a, b = b, a + b

# Get number of terms from user
n = int(input("Enter number of terms: "))

# Generate fibonacci series
fibonacci(n)