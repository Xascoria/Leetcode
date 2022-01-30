class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if encodedText == "" or rows == 0:
            return encodedText
        m = [encodedText[i:i+len(encodedText)//rows] for i in range(0, len(encodedText), len(encodedText)//rows)]
        k = [m[i][i:]+" " for i in range(len(m))]
        #print(k)
        x = ""
        for i in zip(*k):
            x += ''.join(i)
        return x.rstrip()

x = Solution()
print(x.decodeCiphertext("iveo    eed   l te   olc", rows = 4))