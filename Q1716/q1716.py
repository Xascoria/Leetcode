class Solution:
    def totalMoney(self, n: int) -> int:
        a = (n//7 * 28)
        b = 7*( (n//7) * (n//7-1)//2  )
        c = sum(i+n//7 for i in range(1,n%7+1))
        #print(a,b,c)
        return a+b+c

x = Solution()
print( x.totalMoney(20) )