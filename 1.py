def fibonacci_series(n):
    a, b = 0, 1
    fib_series = []

    while a <= n:
        fib_series.append(a)
        a, b = b, a + b

    return fib_series

num = int(input("Enter a number: "))
fibonacci = fibonacci_series(num)
print(f"Fibonacci series up to {num}:")
print(fibonacci)