class Solution:
    def convert(self,s: str, numRows: int) -> str:
        output = ["" for i in range(numRows)]

        i = 0
        while i < len(s):
            for j in range(numRows):
                output[j] += s[i]
                i += 1
                if i >= len(s): break
            if i >= len(s): break
            for j in range(numRows-2):
                output[-2-j] += s[i]
                i += 1
                if i >= len(s): break
        return "".join(output)