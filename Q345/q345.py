class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        for i in range(len(s)):
            if s[i] in vowels:
                ptr1 = i
                break
        else: return s
        for i in range(len(s)-1, -1, -1):
            if s[i] in vowels:
                ptr2 = i
                break
        output_arr = list(s)
        while ptr1 < ptr2:
            output_arr[ptr1], output_arr[ptr2] = output_arr[ptr2], output_arr[ptr1]
            ptr1 += 1
            while output_arr[ptr1] not in vowels:
                ptr1 += 1
            ptr2 -= 1
            while output_arr[ptr2] not in vowels:
                ptr2 -= 1
        return "".join(output_arr)