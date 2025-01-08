# Advanced one-liner: Fibonacci sequence generator
fib = lambda n: (a for a, _ in zip(
    (lambda: [(lambda a=[0, 1]: a.append(a[-1] + a[-2]) or a[-2])() for _ in range(n)])(),
    range(n)
))

# Generate and print the first 10 Fibonacci numbers
print(list(fib(10)))
