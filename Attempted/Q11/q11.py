from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        largest_left = [height[0]]
        largest_right = [height[-1]]

        for i in range(1,len(height)):
            largest_left.append( max(largest_left[-1], height[i]) )
            largest_right.append( max(largest_right[-1], height[-i-1]) )
        # for i in range(len(height)-2, -1, -1):
        #     largest_right.append( max(largest_right[-1], height[i]) )
        #print(largest_left, largest_right[::-1])
        largest_right = largest_right[::-1]
        max_area = 0
        using_left = 0
        for i in range(len(height)-1):
            if largest_left[i] == using_left or largest_left[i]*(len(height)-i) < max_area:
                continue
            cur_left = largest_left[i]
            cur_right = 0
            #print("cl",cur_left)
            for j in range(len(height)-1,i,-1):
                if cur_left*(j-i) < max_area:
                    break
                if largest_right[j] == cur_right:
                    continue
                if min(largest_right[j], cur_left)*(j-i) > max_area:
                    #print(i,j,min(largest_right[j], cur_left)*(j-i))
                    using_left = cur_left
                    cur_right = largest_right[j]
                    max_area = min(largest_right[j], cur_left)*(j-i)
                if largest_right[j] >= cur_left:
                    break
        return max_area
            

x = Solution()
print( x.maxArea([1,2]) )
# arr = [2,3,4,5,18,17,6]
# for i in range(len(arr)-1):
#     for j in range(1,len(arr)):
#         print(i,j, min(arr[i], arr[j])*(j-i))