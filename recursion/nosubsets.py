def subsets(n):
    if n == 0:
        return 1
    else:
        return 2 * subsets(n - 1)


print(subsets(3))
