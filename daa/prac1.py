'''Write a program to calculate Fibonacci numbers and find its step count'''
def fibonacci(n):
    if n <= 0:
        return 0, 1
    elif n == 1:
        return 1, 1
    else:
        fib1, count1 = fibonacci(n - 1)
        fib2, count2 = fibonacci(n - 2)
        return fib1 + fib2, count1 + count2 + 1

n = int(input("Enter the value of n: ")) #end point
fibonacci_number, step_count = fibonacci(n)

print(f"The {n}-th Fibonacci number is {fibonacci_number}")
print(f"Step count for calculating Fibonacci({n}): {step_count}")
