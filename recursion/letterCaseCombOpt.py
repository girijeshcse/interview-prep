

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = []

        def helper(S, i):
            # Base case: there are no more positions left to fill in
            if i == len(S):
                # Append the partial solution to the result
                result.append("".join(S))
            else:  # Recursive case: more positions left to fill in
                if S[i].isdigit():  # If the leftmost blank is a digit
                    # Append it to the partial solution and delegate the rest
                    helper(S, i+1)
                else:  # S[i] is a letter
                    S[i] = S[i].upper()
                    # Append uppercase letter to the partial solution
                    helper(S, i+1)
                    S[i] = S[i].lower()
                    # Append lowercase letter to ther partial solution
                    helper(S, i+1)
                    # .. and delegate the remaining work to a subordinate

        # Root manager implements the overall function by calling the helper function
        helper(list(S), 0)
        # .. with the same string S and i == 0 (subproblem size is the entire string)
        # .. and the partial solution is empty
        return result


mysolution = Solution()
print(mysolution.letterCasePermutation("a1b2c3"))
