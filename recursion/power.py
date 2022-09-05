from unittest import result


def power(n, k):
    """
    calculate n **k
    """
    if k == 0:
        return 1
    else:
        return n * power(n, k - 1)


print(power(2, 5))


def iterative_power(n, k):
    result = 1
    for i in range(k):
        result = result * n
    return result


print(iterative_power(2, 5))
