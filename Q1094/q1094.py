class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        occupants = [0] * 1001
        for numpass, from_stand, to_stand in trips:
            for i in range(from_stand, to_stand):
                occupants[i] += numpass   
        return max(occupants) <= capacity