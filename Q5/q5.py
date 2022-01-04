class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        for i in range(len(s)):
            for j in range(len(s)-1,i,-1):
                if j-i+1 < len(longest):
                    break
                if s[i] == s[j]:  
                    section = s[i:j+1]
                    if section == section[::-1]:
                        longest = section
                        break
                    
        return longest

x = Solution()
print( x.longestPalindrome("aacabdkacaa") )