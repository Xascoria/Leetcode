import random
class Solution:

    def __init__(self, nums: List[int]):
        self.org_lst = nums
        self.shuffled = nums[:]

    def reset(self) -> List[int]:
        return self.org_lst

    def shuffle(self) -> List[int]:
        for i in range(len(self.shuffled)-1, 0, -1):
            j = random.randint(0,i)
            self.shuffled[i],self.shuffled[j] = self.shuffled[j],self.shuffled[i]
        return self.shuffled


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()