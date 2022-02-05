from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        d = {}
        for i,j,k in bookings:
            d[i] = d.get(i, 0) + k
            d[j+1] = d.get(j+1, 0) - k

        output = [0] * n
        cur_need = 0
        for i in range(n):
            cur_need += d.get(i+1,0) 
            output[i] = cur_need
        return output
    

x = Solution()
print( x.corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], 5) )