class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = {}
        for i,j in enumerate(s):
            if j not in char_dict:
                char_dict[j] = (1, i)
            else:
                char_dict[j] = (char_dict[j][0]+1, char_dict[j][1])
        for i in char_dict:
            if char_dict[i][0] == 1:
                return char_dict[i][1]
        return -1

## Alternate
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = {}
        for i in s:
            if i not in char_dict:
                char_dict[i] = 1
            else:
                char_dict[i] += 1
        for i in char_dict:
            if char_dict[i] == 1:
                return s.index(i)
        return -1