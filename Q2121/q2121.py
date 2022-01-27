from typing import List

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        d = {}
        for index, j in enumerate(arr):
            if j not in d:
                d[j] = [index]
            else:
                d[j].append(index)

        output = [0] * len(arr)
        #print(d)
        for i in d:
            left_sum = [0] * len(d[i])
            right_sum  = [0] * len(d[i])
            for j in range(len(d[i])-1):
                left_sum[j+1] = left_sum[j] + d[i][j]
                right_sum[-j-2] = right_sum[-j-1] + d[i][-j-1]
            for j in range(len(d[i])):
                less = d[i][j] * j
                more = (len(d[i])-1-j) * d[i][j]
                # print("INVI")
                # print(d[i][j], less, - sum(d[i][:j]),  sum(d[i][j+1:]), - more)
                # print(less - sum(d[i][:j]) + sum(d[i][j+1:]) - more)
                output[d[i][j]] = less - left_sum[j] + right_sum[j] - more
                
        return output
#[4,2,7,2,4,4,5]
x = Solution()
print( x.getDistances([2,1,3,1,2,3,3]) )

def x(y:List):
    print(y)
x([1,2,3])