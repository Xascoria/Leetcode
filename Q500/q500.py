from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        output = []
        for i in words:
            w = i.lower()
            z = (w[0] in rows[1]) * 1 + (w[0] in rows[2]) * 2
            for j in range(1, len(w)):
                if w[j] not in rows[z]:
                    break
            else:
                output.append(i)
        return output
