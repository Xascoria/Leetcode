from typing import List

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        d = {}
        for i in licensePlate:
            if i.isalpha():
                d[i.lower()] = d.get(i.lower(),0)+1

        cw = ''
        cl = float('inf')
        for w in words:
            for k in d:
                if w.count(k) < d[k]:
                    break
            else: 
                if len(w) < cl:
                    cl = len(w)
                    cw = w
        return cw