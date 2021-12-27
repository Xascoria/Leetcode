class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_str = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                processed_str += i.lower()
        return processed_str == processed_str[::-1]
        