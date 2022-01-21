class Solution:
    def countPoints(self, rings: str) -> int:
        arr = [0] * 10

        for i in range(0, len(rings), 2):
            arr[int(rings[i+1])] |= 2 ** ("RGB".index(rings[i]))

        return arr.count(7)

x = Solution()
print( x.countPoints("B0B6G0R6R0R6G9") )