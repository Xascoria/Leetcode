class Solution:
    def addDigits(self, num: int) -> int:
        total = 0
        for i in map(int,str(num)):
            total += i
            if total > 9:
                total = total - 10 + 1
        return total
        