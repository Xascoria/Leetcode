class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []

        start = nums[0]
        end = nums[0]
        output = []
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start == end:
                    output.append( f"{start}" )
                else:
                    output.append( f"{start}->{end}" )
                start = nums[i]
                end = nums[i]
            else:
                end = nums[i]
        if start == end:
            output.append( f"{start}" )
        else:
            output.append( f"{start}->{end}" )
        return output