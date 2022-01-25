from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height)-1
        #prev_move_is_left = True
        area = min( height[left_pointer], height[right_pointer] ) * (right_pointer-left_pointer)
        while left_pointer != right_pointer:
            if height[left_pointer] > height[right_pointer]:
                right_pointer -= 1
            elif height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                left_pointer += 1
            #print(left_pointer, right_pointer,area)
            area = max(min( height[left_pointer], height[right_pointer] ) * (right_pointer-left_pointer), area)
        return area   

x = Solution()
print( x.maxArea([2,3,4,5,18,17,6]) )
