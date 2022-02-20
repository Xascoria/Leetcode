from typing import List
import heapq

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         occur_dict = {}
#         heap = []

#         for i in range(k):
#             if nums[i] in occur_dict:
#                 occur_dict[nums[i]] += 1
#             else:
#                 occur_dict[nums[i]] = 1
#                 heapq.heappush( heap, -nums[i] )
        
#         output = [-heap[0]]
#         for i in range( len(nums)-k ):
#             occur_dict[nums[i]] -= 1
#             print( nums[i],heap, occur_dict )
#             if nums[i] == -heap[0] and occur_dict[nums[i]] == 0:
#                 heapq.heappop( heap )
#                 while (-heap[0] not in occur_dict) or occur_dict[-heap[0]] == 0:
#                     heapq.heappop( heap )
#             if nums[i+k] not in occur_dict:
#                 occur_dict[ nums[i+k] ] = 1
#                 heapq.heappush( heap, -nums[i+k] )
#             else:
#                 occur_dict[ nums[i+k] ] += 1
#             output.append( -heap[0] )
#         return output

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==1: return nums

        occur_dict = {}
        heap = []

        for i in range(k):
            number = -nums[i]
            if number in occur_dict:
                occur_dict[ number ] += 1
            else:
                heapq.heappush( heap, number )
                occur_dict[ number ] = 1

        output = [-heap[0]]
        for i in range(len(nums)-k):
            num_to_remove = -nums[i]
            occur_dict[ num_to_remove ] -= 1
            if heap[0] == num_to_remove and occur_dict[ num_to_remove ] == 0:
                heapq.heappop( heap )
                while occur_dict[ heap[0] ] == 0:
                    heapq.heappop( heap )
            num_to_add = -nums[i+k]
            if num_to_add in occur_dict and occur_dict[num_to_add] > 0:
                occur_dict[num_to_add] += 1
            else:
                heapq.heappush( heap, num_to_add )
                occur_dict[num_to_add] = 1
            output.append( -heap[0] )
        return output


x = Solution()
print( x.maxSlidingWindow([1,3,-1,-3,5,3,6,7,5,2,3,4,-10,111,2332,1231,23,1,1,2,-1,-2,3,33,213,0,0,0,1,1,2,3,3,3,3,35,5,5], 3) )