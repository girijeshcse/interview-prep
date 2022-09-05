def addseq(n, b1, b2):
    if n == 0:
        return b1
    else:
        return addseq(n - 1, b2, b1+b2)


print(addseq(8, 0, 1))
