import math

class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0: return 1
        
        log2_val = math.log2(num)
        xor_val = 2**(math.ceil(log2_val)+log2_val.is_integer())-1
        return num ^ xor_val

x = Solution()
res = x.findComplement(4)
print(res)
