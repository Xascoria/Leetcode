class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1arr = [0] * 26
        for i in s1:
            s1arr[ord(i)-97] += 1
    
        s2arr = [0] * 26
        for i in range(len(s1)):
            s2arr[ord(s2[i])-97] += 1

        if s1arr == s2arr: return True
        for i in range(len(s1),len(s2)):
            s2arr[ord(s2[i])-97] += 1
            s2arr[ord(s2[i-len(s1)])-97] -= 1

            if s1arr == s2arr:
                return True
        return False


x = Solution()
print( x.checkInclusion("ab", s2 = "eidbaooo") )