class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S:str
        :rtype: List[str]
        """
        result = []

        def helper(S, i, slate):
            # Base case: there are no more postions left
            if i == len(S):
                # The partial solution is the full permulation
                result.append("".join(slate))
                return
            # Recursive Case
            if S[i].isdigit():  # If the leftmost blank is a digit, there is only one thing to do
                slate.append(S[i])  # Add it to partial solution
                # .. and delegate the remaining blanks to a subordinate
                helper(S, i+1, slate)
                slate.pop()  # Slate is mutable so neet to revert any modification done
            else:  # S[i].isalpha()-- if the leftmost blank is a letter, there are two options
                # option 1 is to go with the lowercase letter
                slate.append(S[i].lower())
                # Delegate remaining work to a subordinate
                helper(S, i+1, slate)
                slate.pop()
                # option 2 is to go with the uppercase letter
                slate.append(S[i].upper())
                # Delegate remaining work to a subordinate
                helper(S, i+1, slate)
                slate.pop()
        # Root manager is called with entire string a subproblem definition
        helper(S, 0, [])
        return result


mysolution = Solution()
print(mysolution.letterCasePermutation("a1b2"))
