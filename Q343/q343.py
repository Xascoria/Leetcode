class Solution:
    def integerBreak(self, n: int) -> int:
        arr = [0] * (n+1)
        # for i in range(1,min(10,n+1)):
        #     arr[i] = i
        arr[1] = 1
        for i in range(2,n+1):
            for j in range(1,min(i,10))[::-1]:
                # if i == 5:
                #     print(j, arr[i], max(arr[i], arr[i-j] * j))
                a = arr[i-j]
                if i-j < 10:
                    a = max(a, i-j)
                b = arr[j]

                arr[i] = max(arr[i], a * max(b,j))
        return arr[-1]

x = Solution()
print( x.integerBreak(10) )