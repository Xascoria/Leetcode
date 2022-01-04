class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        k = list(set(s))
        k.sort(key=lambda x:d[x],reverse=1)
        out = ""
        for i in k:
            out += i*d[i]
        return out