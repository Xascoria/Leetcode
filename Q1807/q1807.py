from typing import List
import re

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        dk = {}
        for i,j in knowledge:
            dk['('+i+')'] = j
        p = s.replace('(', ' (').replace(')',') ').split()
        for i in range(len(p)):
            if p[i] in dk:
                p[i] = dk[p[i]]
            elif p[i][0] == "(":
                p[i] = "?"
        return ''.join(p)


        for i,j in knowledge:
            s=s.replace("("+i+")",j)
        return re.sub(r'\([a-z]*\)','?',s)

x = Solution()
a="(fy)(kj)(ege)r"
b=[["uxhhkpvp","h"],["nriroroa","m"],["wvhiycvo","z"],["qsmfeing","s"],["hbcyqulf","q"],["xwgfjnrf","b"],["kfipazun","s"],["wnkrtxui","u"],["abwlsese","e"],["iimsmftc","h"],["pafqkquo","v"],["kj","tzv"],["fwwxotcd","t"],["yzgjjwjr","l"]]

print( x.evaluate(a,b) )