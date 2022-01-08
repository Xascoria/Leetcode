class Solution:
    def trailingZeroes(self, n: int) -> int:
        output = 0
        cur_base = 1
        while n >= 5**cur_base:
            output += n // 5**cur_base
            cur_base += 1
        return output