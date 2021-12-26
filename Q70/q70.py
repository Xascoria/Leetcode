class Solution:
    def climbStairs(self, n: int) -> int:
        possibilities = [1,1] + [0]*(n-2)

        for i in range(len(possibilities)-1):
            for j in range(i+1,min(i+3,len(possibilities))):
                possibilities[j] += possibilities[i]

        return possibilities[n-1]

x = Solution()
ans = x.climbStairs(5)
print("Ans:",ans)