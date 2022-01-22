class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        left = len(cost)
        output = 0
        while left >= 3:
            output += cost[left-1] + cost[left-2]
            left -= 3
        if left == 2:
            output += cost[0] + cost[1]
        elif left == 1:
            output += cost[0]
        return output