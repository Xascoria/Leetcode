class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_hand = minutes * 6
        hour_hand = (hour * 30 + minutes/2) % 360

        return min( abs(min_hand - hour_hand), 360 - abs(min_hand - hour_hand))


x = Solution()
print( x.angleClock(12,30) )