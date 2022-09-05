def fibo(n):
    if n == 0 or n == 1:
        return (n)
    else:
        return (fibo(n - 1) + fibo(n - 2))


print(fibo(8))
for i in range(10):
    print(fibo(i))
