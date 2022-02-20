from re import A
from typing import List

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        c = -1
        for i in nums:
            if i%2:
                c = i
                break
        else:
            c = min(nums)

        if c % 2:
            poss = [c, c*2]
        else:
            poss = [c]
            while c%2 == 0:
                c//= 2
                poss.append(c)
        
        visited_set = set()

        ranges = [[poss[i], poss[i]] for i in range(len(poss))]
        for num in nums:
            if num in visited_set:
                continue
            visited_set.add(num)

            if num%2:
                spreads = [num, num*2]
            else:
                spreads = [num]
                while num%2 == 0:
                    num//= 2
                    spreads.append(num)


            for this_range in ranges:
                start, end = this_range
                for s in spreads:
                    if start <= s <= end:
                        break
                else:
                    lower = [(abs(s-start), s) for s in spreads]
                    upper = [(abs(s-end), s) for s in spreads]
                    
                    c = min(lower)
                    d = min(upper)
                    

                    if c[0] < d[0]:
                        this_range[0] = c[1]
                    elif c[0] > d[0]:
                        this_range[1] = d[1]
                    else:
                        if c[1] < this_range[0]:
                            this_range[0] = c[1]
                        else:
                            this_range[1] = c[1]
            print(ranges)
        print(ranges)
        return min(j-i for i,j in ranges)


    
x = Solution()
#print( x.minimumDeviation([399,908,648,357,693,502,331,649,596,698]) )

import heapq
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        for i in nums:
            start = i
            while start%2 == 0:
                start //= 2
            heapq.heappush( heap, [start, i] )
        
        odd_max = max(i[0] for i in heap)
        output = float('inf')
        while len(heap) == len(nums):
            a,b = heapq.heappop( heap )
            output = min(output, odd_max - a)

            if a < b or a%2 == 1:
                odd_max = max(odd_max, a*2)
                heapq.heappush(heap, [a*2, b] )
        return output