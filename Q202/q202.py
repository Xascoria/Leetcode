class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1:
            n = sum(map(lambda x:int(x)**2, str(n)))
            if n in (2,4):
                return False
        return True