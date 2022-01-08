class Solution:
    def longestPalindrome(self, s: str) -> int:
        occurance_dict = {}
        for i in s:
            if i not in occurance_dict:
                occurance_dict[i] = 1
            else:
                occurance_dict[i] += 1
        even = sum(i for i in occurance_dict.values() if i % 2 == 0)
        odd = [i for i in occurance_dict.values() if i % 2]
        if len(odd) == 0:
            return even
        return even + odd[0] + sum(i-1 for i in odd[1:])

        