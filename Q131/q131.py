from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # def recursion(partition_dict,cur_index):
        #     if cur_index == len(s):
        #         return partition_dict
        #     if cur_index == 0:
        #         partition_dict[1] = [[s[0]]]
        #         recursion(partition_dict, cur_index+1)
        #         return
        partition_dict = {}
        def recursion(cur_index):
            if cur_index == len(s)+1:
                return partition_dict
            for i in range(cur_index):
                string = s[i:cur_index] 
                if string == string[::-1]:
                    if i == 0:
                        partition_dict[cur_index] = [[string]]
                    elif cur_index - len(string) in partition_dict:
                        if cur_index not in partition_dict:
                            partition_dict[cur_index] = []
                        for series in partition_dict[cur_index-len(string)]:
                            partition_dict[cur_index] += [series + [string]]
            recursion(cur_index+1)

        recursion(1)
        return partition_dict[len(s)]
        

x = Solution()
print( x.partition("aabb") )

