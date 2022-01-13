class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        value_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for i,j in enumerate(s):
            if j == "I" and i+1 != len(s) and s[i+1] in "VX":
                output -= 1
            elif j == "X" and i+1 != len(s) and s[i+1] in "LC":
                output -= 10
            elif j=="C" and i+1 != len(s) and s[i+1] in "DM":
                output -= 100
            else:
                output += value_dict[j]
        return output