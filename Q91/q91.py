class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1: return int(s!="0")

        arr = [0] * len(s)
        arr[-1] = int(s[-1] != "0")
        if s[-2] == "0":
            arr[-2] = 0
        else:
            if s[-1] == '0':
                if int(s[-2:]) <= 26:
                    arr[-2] = 1
                else:
                    return 0
            else:
                arr[-2] = 1 + (int(s[-2:]) <= 26)

        
        for i in range(len(s)-3, -1, -1):
            if s[i] == "0":
                arr[i] = 0
            else:
                if s[i+1] == '0':
                    if int(s[i:i+2]) <= 26:
                        arr[i] = arr[i+2]
                    else:
                        return 0
                else:
                    arr[i] = arr[i+1] + (int(s[i:i+2]) <= 26)*arr[i+2]
        
        #print(arr)
        return arr[0]