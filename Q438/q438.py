class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        parr = [0] * 26
        for i in p:
            parr[ord(i)-97] += 1
        
        sarr = [0] * 26
        
        output = []
        for i in range(len(p)):
            sarr[ ord(s[i])-97 ] += 1
        
        if sarr == parr:
            output.append(0)

        for i in range( len(s)-len(p) ):
            sarr[ ord(s[i])-97 ] -= 1
            sarr[ ord(s[i+len(p)])-97 ] += 1
            if sarr == parr:
                output.append(i+1)
        return output
