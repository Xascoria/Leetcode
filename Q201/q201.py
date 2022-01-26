class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        if left == 0 or right == 0:
            return 0

        a = math.log2(left)
        b = math.log2(right)
        if int(a) == int(b):
            start = left
            for i in range(left+1, right+1):
                start &= i
            return start
        return 0