arr = [23, 34, 12, 1, 2, 5, 78, 23]
n = len(arr)


def insertionSort(arr, n):
    if (n <= 1):
        return
    insertionSort(n-1)
    # now insert the nth element into its place
    j = n - 1
    while j >= 1 and (arr[j] > arr[j + 1]):
        arr[j], arr[j + 1] = arr[j+1], arr[j]
        j -= 1
    print(arr)


insertionSort(arr, n=len(arr))
