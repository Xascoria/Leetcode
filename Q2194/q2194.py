class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        a,b,_,c,d = s
        out = []
        for i in range(ord(a),ord(c)+1):
            for j in range(int(b),int(d)+1):
                out.append( chr(i)+str(j) )
        return out