class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s = 1
        while True:
            if s*s == num:
                return True
            if s*s > num:
                return False
            s += 1
        