class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        filtered = ''.join([i for i in s if i != "-"])[::-1]
        out = '-'.join([ filtered[i:i+k] for i in range(0, len(filtered), k) ] )
        #print(out)
        return out.upper()[::-1]

x = Solution()
print( x.licenseKeyFormatting("2-5g-3-J", 2) )