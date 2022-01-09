from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12: return []
        def recursion(prev_nums, cur_num, current_index):
            if len(prev_nums) == 4 and current_index != len(s):
                return []

            if current_index == len(s):
                if len(prev_nums) == 3:
                    return [prev_nums+[cur_num]]
                return []

            output = []
            if len(cur_num) != 0 and 0 <= int(cur_num) <= 255:
                output += recursion(prev_nums+[cur_num], s[current_index], current_index+1)

            new_num = cur_num + s[current_index]
            if len(new_num) > 1 and new_num[0] == "0":
                return output
            elif not 0<=int(new_num)<= 255:
                return output
            else:
                output += recursion(prev_nums, new_num, current_index+1)
            return output
        return map(".".join,recursion([], "", 0) )

x = Solution()
print( x.restoreIpAddresses("25525511135") )