class Solution:
    def recursion(self, current, remain):
        if len(remain) == 0:
            return [tuple(current)]

        output = []
        for i,j in enumerate(remain):
            output += self.recursion(current+[j], remain[:i]+remain[i+1:])
        return output
            
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(self.recursion([],nums))