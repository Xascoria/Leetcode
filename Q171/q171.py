class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        output = 0
        alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i,j in enumerate(columnTitle[::-1]):
            output += alpha.index(j) * 26**i
        return output
            
        