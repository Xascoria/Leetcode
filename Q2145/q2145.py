from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        zero_b_arr = [0]
        cur_val = 0
        for i in differences:
            cur_val += i
            zero_b_arr.append( cur_val )
        
        a,b = min(zero_b_arr), max(zero_b_arr)

        # print(zero_b_arr)
        # print(a,b,b+lower-a)
        #return max(0, upper - (b+lower-a)+1)
        return max(0, upper - b-lower+a+1)

x = Solution()

print( x.numberOfArrays([1,-3,4],1,6) )