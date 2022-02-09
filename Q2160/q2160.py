#2160
class Solution:
    def minimumSum(self, num: int) -> int:
        a = sorted(str(num))
        num1 = a[0] + a[2]
        num2 = a[1] + a[3]
        return int(num1) + int(num2)