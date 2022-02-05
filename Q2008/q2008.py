class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        arr = [0] * (n + 1)
        cur_ptr = 0
        b4max = 0

        for i in range(1, n+1):
            arr[i] = max(arr[i], b4max)
            while len(rides) > cur_ptr and rides[cur_ptr][0] == i:
                arr[rides[cur_ptr][1]] = max(arr[rides[cur_ptr][1]], arr[i] + rides[cur_ptr][2] + rides[cur_ptr][1] - rides[cur_ptr][0])
                cur_ptr += 1
            b4max = max(b4max, arr[i])
        return b4max