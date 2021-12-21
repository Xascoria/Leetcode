class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        arr = [*zip(*strs)]
        out = 0
        for i in arr:
            if len(set(i)) == 1: out += 1
            else: break
        return strs[0][:out]
        