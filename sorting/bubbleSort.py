arr = [23, 34, 12, 1, 2, 5, 78, 23]
arr = [1, 2, 5, 12, 23, 23, 34, 78]


def bubbleSort(A):
    j = 0
    for start in range(len(A)):
        for i in range(len(A)-1, start, -1):
            if A[i-1] > A[i]:
                A[i-1], A[i] = A[i], A[i-1]
                j += 1
    print(A)
    print(j)


bubbleSort(arr)
