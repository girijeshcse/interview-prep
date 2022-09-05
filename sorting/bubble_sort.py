# Goal: Sort an array called nums which has n integres: nums[0....n-1]
# Bubble sort

nums = [23, 34, 12, 1, 2, 5, 78, 23]
# i in 0 to n-1
for i in range(len(nums)):
    # ith iteration: Find the minimum element from index i to n-1, and put it in index i
    # Find the min element by scanning the array from index n-1 to index i+1, and swapping the current element
    # with the element to its left, if they are out of order. i.e. bubble thhhe minimum elemnt from right to left
    for j in range(len(nums)-1, i, -1):
        if nums[j] < nums[j-1]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
print(nums)
