class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        cur = 0
        i = 0
        while cur < neededApples:
            i += 2
            cur += 3*i*i
        return i*4