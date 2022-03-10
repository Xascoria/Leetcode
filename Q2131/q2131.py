from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq_dict = {}

        for i in words:
            freq_dict[i] = freq_dict.get(i,0)+1

        output = 0
        middle_occupied = False
        for i in range(97, 123):
            for j in range(i+1, 123):
                if chr(i)+chr(j) in freq_dict and chr(j)+chr(i) in freq_dict:
                    output += min(freq_dict[chr(i)+chr(j)],freq_dict[chr(j)+chr(i)])*4

            if chr(i)+chr(i) in freq_dict:
                x = freq_dict[chr(i)+chr(i)]
                if x%2:
                    middle_occupied = True
                output += (x//2) * 4
        return output + (middle_occupied * 2)
        

x = Solution()
print( x.longestPalindrome(['ab']) )