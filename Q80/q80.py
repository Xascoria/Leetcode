class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return

        cur_val = nums[0]
        cur_count = 1
        replace_ptr = -1
        for i in range(1,len(nums)):
            if nums[i] == cur_val:
                cur_count += 1
                if cur_count > 2:
                    if replace_ptr == -1:
                        replace_ptr = i
                else:
                    if replace_ptr > 0:
                        nums[replace_ptr] = cur_val
                        replace_ptr += 1
            else:
                cur_val = nums[i]
                cur_count = 1
                if replace_ptr > 0:
                    nums[replace_ptr] = cur_val
                    replace_ptr += 1
        
        if replace_ptr == -1:
            return len(nums)
        return replace_ptr