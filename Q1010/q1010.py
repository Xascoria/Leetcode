from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        divi_count = [0]*60
        for i in time:
            divi_count[i%60] += 1
        output = 0
        for i in range(1,30):
            output += divi_count[60-i]*divi_count[i]
        output += (divi_count[0]-1)*divi_count[0]//2 + (divi_count[30]-1)*divi_count[30]//2
        return output

## Alternate solution with dictionary
## Faster sometimes
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d={}
        for i in time:
            if i%60 not in d:d[i%60]=1
            else: d[i%60] += 1
        output = 0
        for i in range(1,30):
            output += d.get(i,0)*d.get(60-i,0)
        output += (d.get(30,0)-1)*d.get(30,0)//2 + (d.get(0,0)-1)*d.get(0,0)//2
        return output

x = Solution()
print( x.numPairsDivisibleBy60([30,20,150,100,40]) )