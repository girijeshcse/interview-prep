def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result


print(factorial(5))

print(fact(5))
