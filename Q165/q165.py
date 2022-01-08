class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1arr = [*map(int, version1.split("."))]
        v2arr = [*map(int, version2.split("."))]
        for i,j in zip(v1arr, v2arr):
            if i>j:
                return 1
            elif i<j:
                return -1
        if len(v1arr) == len(v2arr):
            return 0
        if len(v1arr) > len(v2arr):
            remains = v1arr[len(v2arr):]
            if len(set(remains)) == 1 and remains[0] == 0:
                return 0
            return 1
        remains = v2arr[len(v1arr):]
        if len(set(remains)) == 1 and remains[0] == 0:
            return 0
        return -1

x = Solution()
print( x.compareVersion("1.0.0.01.1.2.3", "1.0.0.1") )