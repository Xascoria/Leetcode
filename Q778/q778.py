class Solution:
    def rotatedDigits(self, n: int) -> int:
        output = 0
        for i in range(2,n+1):
            p=str(i)
            if "3" in p or "4" in p or "7" in p:
                continue
            elif "2" in p or "5" in p or "6" in p or "9" in p:
                output += 1
        return output