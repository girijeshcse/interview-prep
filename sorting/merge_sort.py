# Goal: Sort an array called nums which has n integres: nums[0....n-1]
# Merge sort

nums = [23, 34, 12, 1, 2, 5, 78, 23]


def helper(A, start, end):
    # Base case: Sub problem of size = 0 or 1 means nothing to do
    if start >= end:
        return

    # Recursive case: python

    # To make the two halves, find the midpoint
    mid = (start + end)//2
    # left half = nums[start...mid] and right half is nums[mid+1..end]
    # Sort left half
    helper(A, start, mid)
    # Sort right half
    helper(A, mid+1, end)
    # Merge the two sorted subarrays via a two pointer pass
    i = start
    j = mid+1
    aux = []
    while i <= mid and j <= end:
        if A[i] <= A[j]:  # "=" in "<=" importand for stability
            aux.append(A[i])
            i += 1
        else:  # A[i] > A[j]
            aux.append(A[j])
            j += 1
    # Gather up remaining elements from the subarray whose pointer did not jump off the right edge
    while i <= mid:
        aux.append(A[i])
        i += 1
    while j <= end:
        aux.append(A[j])
        j += 1

    # Copy the elements from the temporary aux space back into the oiginal subarray
    A[start:end+1] = aux
    print(A)


helper(nums, 0, len(nums) - 1)
