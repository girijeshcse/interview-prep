

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[list[int]]
        """
        result = []

        def helper(S, i, slate):
            # Base case: No more elements left to be examined
            if i == len(S):
                # Add the partial solution as a subset
                result.append(slate[:])
            else:  # Recursive case:
                # Exclude S[i]
                helper(S, i+1, slate)
                # Include S[i]
                slate.append(S[i])
                helper(S, i+1, slate)
                slate.pop()
        helper(nums, 0, [])
        return result


mysolution = Solution()
print(mysolution.subsets([1, 2, 3]))
