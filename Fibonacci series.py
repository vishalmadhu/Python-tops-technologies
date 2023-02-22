n = int(input("enter number: "))

a, b = 0, 1
fib_series = []

for i in range(n+1):
    if a > n:
        break
    fib_series.append(a)
    a, b = b, a + b
print("The Fibonacci series is", fib_series)
