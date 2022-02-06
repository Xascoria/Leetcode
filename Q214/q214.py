
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s==s[::-1]: return s
        center_ptr = len(s)//2 - 1
        left_ptr = center_ptr - 1
        right_ptr = center_ptr + 1
        while left_ptr != -1 and center_ptr != 0:
            if s[left_ptr] == s[right_ptr]:
                left_ptr -= 1
                right_ptr += 1
            else:
                center_ptr -= 0.5
                left_ptr = center_ptr - 1
                right_ptr = center_ptr + 1
        if center_ptr == 0:
            return s[1:][::-1] + s
        return s[right_ptr:][::-1]+s

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s==s[::-1]: return s
        has_center = len(s)%2 == 0
        if len(s)%2 == 0:
            center_ptr = len(s)//2 - 1
            left_ptr = center_ptr - 1
            right_ptr = center_ptr + 1
        else:
            center_ptr = len(s)//2
            left_ptr = center_ptr - 1
            right_ptr = center_ptr 
        while left_ptr != -1 and center_ptr != 0:
            if s[left_ptr] == s[right_ptr]:
                left_ptr -= 1
                right_ptr += 1
            else:
                if has_center:
                    left_ptr = center_ptr - 1
                    right_ptr = center_ptr
                else:
                    center_ptr -= 1
                    left_ptr = center_ptr - 1
                    right_ptr = center_ptr + 1
                has_center = not has_center
        if center_ptr == 0:
            return s[1:][::-1] + s
        return s[right_ptr:][::-1]+s


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        inverted = s[::-1]
        for i in range(len(s)+1):
            if s.startswith(inverted[i:]):
                return inverted[:i] + s