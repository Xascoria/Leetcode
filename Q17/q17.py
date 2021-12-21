from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums_mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        def recursion(digits_left, cur_str):
            if len(digits_left) == 0:
                return [cur_str]

            intval = int(digits_left[0])
            if len(nums_mapping[intval]) == 0:
                return recursion(digits_left[1:], cur_str)

            output = []
            for newchar in nums_mapping[intval]:
                output += recursion(digits_left[1:], cur_str + newchar)
            return output
        
        if digits == "": return []
        return recursion(digits, "")