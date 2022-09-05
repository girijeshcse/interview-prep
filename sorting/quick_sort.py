# Sort an array called nums which has n integres: nums[0....n-1]
# Quick sort

import random

nums = [23, 34, 12, 1, 2, 5, 78, 23]


def helper(A, start, end):
    # Base case: Subproblem of size = 0 or 1 means nothing to do
    if start >= end:
        return

    # Recursive case: Subproblem size at least 2, so cut the subarray into two halves and delegate the sorting
    # work to two other people hired under you
    # To make the two halves, partition the array around a random value
    pindex = random.randint(start, end)
    # move it to extreme left
    A[pindex], A[start] = A[start], A[pindex]
    orange = start
    for green in range(start+1, end+1):  # Both index are inclusive
        if A[green] < A[start]:
            orange += 1
            A[green], A[orange] = A[orange], A[green]
    # Now move the pivot at the boundary of the orange and green regions
    A[start], A[orange] = A[orange], A[start]
    # pivot is now at the orange index. Split the array into two partitions, and delegate their sorting work to two people under you.
    helper(A, start=start, end=orange-1)  # Sort left partition
    helper(A, start=orange+1, end=end)  # Sort right partition
    print(A)


helper(nums, 0, len(nums) - 1)
