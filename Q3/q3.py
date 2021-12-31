class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)

        output = 1
        start_index = 0
        end_index = 1
        while end_index < len(s):
            while s[end_index] not in s[start_index:end_index]:
                end_index += 1
                if end_index == len(s):
                    break
            if end_index - start_index > output:
                output = end_index - start_index
            output = max(output, end_index - start_index)
            start_index += 1
            if end_index == start_index:
                end_index += 1
                if end_index == len(s):return output
            print(start_index,end_index)
        return output
            
x = Solution()
print( x.lengthOfLongestSubstring("au") )