from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        d = {}
        hand.sort()
        for i in hand:
            d[i] = d.get(i, 0) + 1
        for i in hand:
            if d[i] == 0:
                continue

            for j in range(groupSize):
                if d.get(i+j, 0) == 0:
                    return False
                d[i+j] -= 1
        return True

