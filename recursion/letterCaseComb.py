
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S:str
        :rtype: List[str]
        """
        result = []

        def helper(S, i, slate):
            # Base case: there is no more positions left to fill in
            if i == len(S):
                # Append the partial solution to the result
                result.append(slate)
            else:  # Recursive case: more positions left to fill in
                if S[i].isdigit():  # If the leftmost blank is a digit
                    # Append it to the partial solution and delegate the rest
                    helper(S, i+1, slate=slate+S[i])
                else:  # S[i] is a letter
                    # Append uppercase letter to the partial solution
                    helper(S, i+1, slate=slate+S[i].upper())
                    # Append lowercase letter to the partial solution
                    helper(S, i+1, slate=slate+S[i].lower())
                    # .. and delegate the remaining work to a subordinate

        # Root manager implements the overall function by calling the helper function
        helper(S, 0, "")
        # ... with the same string S and i = 0(subproblem size is the entire string)
        # ... and the partial solution is empty
        return result


mysolution = Solution()
print(mysolution.letterCasePermutation("a1b2"))
