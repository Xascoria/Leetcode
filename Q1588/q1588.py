from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        multipliers = [0] * len(arr)
        for length in range(3, len(arr)+1, 2):
            for i in range(0, len(arr)-length+1):
                for j in range(length):
                    multipliers[i+j] += 1
            #print( multipliers )
        return sum(arr) + sum(i*j for i,j in zip(arr, multipliers))

x = Solution()
print( x.sumOddLengthSubarrays([1,4,2,5,3,0]) )