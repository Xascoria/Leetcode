class Solution:
    def zeroFilledSubarray(self, nums) -> int:
        cur_length = 0
        output = 0
        for i in nums:
            if i == 0:
                cur_length += 1
            else:
                if cur_length:
                    output += cur_length * (cur_length+1)//2
                cur_length = 0
        
        return output + cur_length * (cur_length+1)//2