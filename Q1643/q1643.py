from typing import List
import math

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        v_count,h_count = destination
        upper_bound = math.factorial(v_count+h_count) // math.factorial(v_count) // math.factorial(h_count)
        lower_bound = 0
        output = ""
        k -= 1
        while v_count + h_count > 0:
            middle_bound = (h_count * (upper_bound-lower_bound))//(v_count+h_count) + lower_bound
            # print(output)
            # print(lower_bound, middle_bound, upper_bound)
            # print( h_count/(v_count+h_count), upper_bound-lower_bound )
            # print( v_count, h_count )
            if k < middle_bound: #or (middle_bound == 0 and lower_bound == 0):
                output += "H"
                h_count -= 1
                upper_bound = middle_bound

            else:
                output += "V"
                v_count -= 1
                lower_bound = middle_bound
        return output


x = Solution()
print('ans',x.kthSmallestPath([5,7],331))