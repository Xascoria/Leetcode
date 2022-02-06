class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        #right_count = [0] * 26
        right_count = {}
        for i in s:
            right_count[ord(i) - 97] = right_count.get(ord(i)-97,0) + 1
        #left_count = [0] * 26
        left_count = {}
        left_count[ord(s[0]) - 97] = 1
        right_count[ord(s[0]) - 97] -= 1
        right_count[ord(s[1]) - 97] -= 1
        output_set = set()
        for pivot in range(1, len(s)-1):
            for ind in range(26):
                if left_count.get(ind,0) > 0 and right_count.get(ind,0) > 0:
                    output_set.add( ord(s[pivot])*100 + ind )
            left_count[ord(s[pivot]) - 97] = left_count.get(ord(s[pivot]), 0) + 1
            right_count[ord(s[pivot+1]) - 97] -= 1
        return len(output_set)

x = Solution()
print( x.countPalindromicSubsequence("aabca") )