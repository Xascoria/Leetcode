from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        a = [*map(str,nums)]
        max_len = len(max(a,key=len))
        def tie_breaker(num_str):
            outstr = num_str
            while len(outstr) < max_len:
                outstr += outstr
            output = int(outstr[-max_len:])
            print("tie",num_str, output)
            return output

        def order_func(num_str):
            while len(num_str) < max_len:
                num_str += num_str
            output = int(num_str[:max_len])
            return output
            
        a.sort(key=tie_breaker,reverse=1)
        #print(a)
        a.sort(key=order_func, reverse=1)
        if len(set(a)) == 1 and a[0] == "0":
            return "0"
        return "".join(a)

x = Solution()
print( x.largestNumber([432,43243]) )
