from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        seq = "123456789"
        ls = str(low)
        hs = str(high)
        ptr = seq.index(ls[0])
        cur_len = len(ls)
        #print(ptr)
        if int(seq[ptr:ptr+cur_len]) < low:
            ptr += 1
            if int(seq[ptr:ptr+cur_len]) < low:
                ptr = 0
                cur_len += 1
        if cur_len == 10:
            return []
        output = []
        while True:
            if ptr == 0 and len(hs) > cur_len:
                output += [int(seq[i:i+cur_len]) for i in range(0, len(seq)-cur_len+1)]
            else:
                for i in range(ptr, len(seq)-cur_len+1):
                    ans = int(seq[i:i+cur_len])
                    if ans <= high:
                        output.append(ans)
                    else:
                        return output
                if len(hs) == cur_len:
                    return output
            ptr = 0
            cur_len += 1
            


x = Solution()
print( x.sequentialDigits(178546104,812704742) )