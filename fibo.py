def fibonacci_triangle(n):
    """Generate triangle with Fibonacci numbers"""
    def fibonacci(k):
        if k <= 1:
            return k
        return fibonacci(k-1) + fibonacci(k-2)

    fib = ""
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(fibonacci(j + i))
        # Format output
        spaces = " " * (n - i) * 3
        fib+=spaces + " ".join(f"{num:3d}" for num in row)+"<br>"

    return fib
