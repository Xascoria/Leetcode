class Solution:
    def lastSubstring(self, s: str) -> str:
        pack = []
        cur_char = 'a'
        for i,j in enumerate(s):
            if j > cur_char:
                cur_char = j
                pack = [i]
            elif j == cur_char:
                pack.append(i)
        
        next_in_line = 1
        while len(pack) != 1:
            new_pack = []
            cur_char = 'a'
            for i in pack:
                if i+next_in_line != len(s):
                    if s[i+next_in_line] > cur_char:
                        cur_char = s[i+next_in_line]
                        new_pack = [i]
                    elif s[i+next_in_line] == cur_char:
                        new_pack.append(i)
            while len(new_pack) != 1 and new_pack[-1]-next_in_line == new_pack[-2]:
                new_pack.pop()
            
            pack = new_pack
            next_in_line += 1
        return s[pack.pop():]

x = Solution()
print( x.lastSubstring("abababab") )