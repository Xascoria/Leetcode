class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        ans = self.countAndSay(n-1)
        curchar = ans[0]
        count = 1
        fs = ""
        for i in range(1,len(ans)):
            if curchar != ans[i]:
                fs += str(count) + curchar 
                count = 1
                curchar = ans[i]
            else:
                count += 1
        fs += str(count) + curchar 
        return fs
                