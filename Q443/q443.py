from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        cur_char = chars[0]
        count = 1
        ptr = 0

        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                chars[ptr] = cur_char
                ptr += 1
                if count > 1:
                    for j in list(str(count)):
                        chars[ptr] = j
                        ptr += 1
                cur_char = chars[i]
                count = 1
        chars[ptr] = cur_char
        ptr += 1
        if count > 1:
            for i in list(str(count)):
                chars[ptr] = i
                ptr += 1

        return ptr

x = Solution()
print( x.compress( ["a","b","b","b","b","b","b","b","b","b","b","b","b"]) )