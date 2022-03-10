from typing import List

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1

        output = 0
        for i in range(1, len(target)):
            #print('bruh', target[:i])
            if target[:i] in d and target[i:] in d:
                p = d[target[:i]]
                q = d[target[i:]]
                if target[:i] == target[i:]:
                    output += (p-1) * p
                else:
                    output += (p*q)
        return output

x = Solution()
print( x.numOfPairs([], '12345') )