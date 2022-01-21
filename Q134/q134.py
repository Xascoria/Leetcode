class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        cur_start_station = 0
        cur_fuel = 0
        for i in range( len(gas) ):
            cur_fuel += gas[i] - cost[i]
            if cur_fuel < 0:
                cur_start_station = i

        return cur_start_station