from unittest import result


def binary_string(n):
    if n == 1:
        return ['0', '1']
    else:
        prev = binary_string(n - 1)
        result = []
        for s in prev:
            result.append(s + '0')
            result.append(s + '1')
        return result


# print(binary_string(3))

# Lets do it in iterative way


def binaryString(n):
    result = ['0', '1']
    for iter in range(2, n+1):
        new_result = []
        for s in result:
            new_result.append(s + '0')
            new_result.append(s + '1')
        result = new_result
    print(result)


# binaryString(3)

# lets try another method
def bshelper(slate, n):
    if n == 0:
        print(slate)
    else:
        bshelper(slate=slate + "0", n=n-1)
        bshelper(slate=slate + '1', n=n-1)


def bstr(n):
    bshelper(" ", n)


print(bstr(3))
