#767
class Solution:
    def reorganizeString(self, s: str) -> str:
        d = {}
        for i in s:
            d[i] = d.get(i,0)+1
        allsum = sum(d.values())
        maxval = max(d.values())
        if maxval-1 > allsum - maxval:
            return ""
        arr = [*d.keys()]
        arr.sort(key=lambda x:d[x],reverse=True)
        out = [None] * len(s)
        cur_ptr = 0
        for i in range(0, len(out), 2):
            out[i] = arr[cur_ptr]
            d[arr[cur_ptr]] -= 1
            if d[arr[cur_ptr]] == 0:
                cur_ptr += 1
        for i in range(1, len(out), 2):
            out[i] = arr[cur_ptr]
            d[arr[cur_ptr]] -= 1
            if d[arr[cur_ptr]] == 0:
                cur_ptr += 1
        return ''.join(out)