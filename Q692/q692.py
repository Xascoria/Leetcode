from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for i in words:
            d[i] = d.get(i,0)+1
        arr = []
        for i in d:
            arr.append(  (d[i], i))
        arr.sort(key=lambda x:(len(words)-x[0], x[1]) )
        print(arr)
        return [i[1]for i in arr[:k]]