class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power = 15
        while n:
            if n >= 3**power:
                c = n//(3**power)
                if c > 1:
                    return False
                n %= (3**power)
            power -= 1
        return True