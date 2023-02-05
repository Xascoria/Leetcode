from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        type_arr = [-1,-1,-1]
        type_str = "MPG"

        for index, j in enumerate(garbage[::-1]):
            f_index = 0
            for k, l in zip(type_arr, type_str):
                if k == -1 and l in j:
                    type_arr[f_index] = len(garbage) - index - 1
                f_index += 1
            if -1 not in type_arr:
                break
        
        output = 0
        for i in range( len(type_str) ):
            if type_arr[i] != -1:
                if type_arr[i] != 0:
                    output += sum(travel[:type_arr[i]])
        return output + sum(map(len,garbage))


out = Solution().garbageCollection(["G","P","GP","GG"], travel = [2,4,3])

print(out)