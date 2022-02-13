class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        out = ""
        for i,j in enumerate(nums):
            out += "10"[int(j[i])]
        return out