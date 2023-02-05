class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = [0]
        ptr = 0
        for i,j in enumerate(s):
            if j == "(":
                ptr += 1
                if ptr == len(score):
                    score.append(0)
            else:
                if s[i-1] == '(':
                    score[-1] += 1
                else:
                    k = score.pop()
                    score[-1] += 2*k
        return sum(score)

x = Solution()
print( x.scoreOfParentheses('(())()((()()))') )