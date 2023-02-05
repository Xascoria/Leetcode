from typing import List
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        arr = [1] * (10**5 + 1)

        arr[0] = arr[1] = 0
        for i in range(2, len(arr)):
            if arr[i]:
                arr[i+i::i] = [0] * len(arr[i+i::i])

        s = 0
        for num in nums:
            for i in range(2, math.ceil(num**0.5)+1):
                if num%i == 0 and num//i != i:
                    if arr[i] and arr[num//i]:
                        s += 1+num+num//i+i
                        break
                    if arr[i] and i*i == num//i:
                        s += 1+num+num//i+i
                        break

        return s
        

x = Solution()
print( x.sumFourDivisors([1,2,3,4,5,6,7,8,9,10]) )
