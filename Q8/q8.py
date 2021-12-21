class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "": return 0
        
        for i in range(len(s)):
            if s[i] != " ": 
                break
                
        if i-1 == len(s)-1: return 0
        
        final = ""
        if s[i] in "+-":
            final += s[i]
            i += 1
        for j in range(i,len(s)):
            if s[j] not in "0123456789":
                break
            final += s[j]
        
        
        if final in "+-" or final == "":
            return 0
        fn = int(final)
        if fn > 2**31 - 1:
            return  2**31 - 1
        if fn < -2**31:
            return -2**31
        return fn