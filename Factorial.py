def factorial(n):
    if n == 1:
        return n;
    return n * factorial(n -1);

print(factorial(5))


def fibonacci(n):
    if n <= 1:
        return 1;
    return fibonacci(n -1) + fibonacci(n -2);

print(fibonacci(5))