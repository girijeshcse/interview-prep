# Goal: Sort an array called nums which has n integres: nums[0....n-1]
# Insertion sort

nums = [23, 34, 12, 1, 2, 5, 78, 23]
# i in 0 to n-1
for i in range(len(nums)):
    # ith iteration: keep nums[0..i] sorted. nums[i] may not be in its right place,
    # so insert it wherever it should go
    j = i - 1
    curr = nums[i]
    while j >= 0 and nums[j] > curr:
        nums[j+1] = nums[j]
        j -= 1

    nums[j + 1] = curr

print(nums)
