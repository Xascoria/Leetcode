class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else: 
                d[i] += 1
        cur_max = 0
        cur_val = 0
        for i in d:
            if d[i]> cur_max:
                cur_val = i
                cur_max = d[i]
        return cur_val
        