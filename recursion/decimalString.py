def dshelper(slate, n):
    if n == 0:
        print(slate)
    else:
        for i in range(10):
            dshelper(slate=slate + str(i), n=n - 1)


def decimalString(n):
    dshelper("", n)


decimalString(2)
