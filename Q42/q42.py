from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left_peaks = [0] * len(height)
        right_peaks = [0] * len(height)
        for i in range(1,len(height)):
            left_peaks[i] = max(left_peaks[i-1], height[i-1])
        for i in range(len(height)-2,-1,-1):
            right_peaks[i] = max(right_peaks[i+1], height[i+1])
        output = 0
        for i in range(len(height)):
            surrounding = min(left_peaks[i], right_peaks[i])
            if height[i] < surrounding:
                output += surrounding - height[i]
        
        return output

x = Solution()
print( x.trap([0,1,0,2,1,0,1,3,2,1,2,1]) )