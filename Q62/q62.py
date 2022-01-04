class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        bottom = [1]*n
        top = [1]*n

        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                top[j] = bottom[j] + top[j+1]
            bottom = top[:]
        return top[0]

x = Solution()
print( x.uniquePaths(3,7) )