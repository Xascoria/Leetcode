from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [float("inf")] * (amount + 1)
        arr[0] = 0
        for i in range(1, len(arr)):
            for c in coins:
                if i-c >= 0:
                    arr[i] = min(arr[i], arr[i-c]+1)

        if arr[-1] == float("inf"):
            return -1
        return arr[-1]

x = Solution()
print( x.coinChange([1,2,5],11) )