class Solution:
    def bitwiseComplement(self, n: int) -> int:
        a = bin(n)[2:]
        b = ["0"if i=="1" else "1" for i in a]
        return int("".join(b),2)