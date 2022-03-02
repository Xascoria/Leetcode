class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            arr = queryIP.split(".")
            if len(arr) != 4:
                return "Neither"
            for i in arr:
                try:
                    c = int(i)
                    if len(str(c)) != len(i):
                        return "Neither"
                    if not (0<=c<=255):
                        return "Neither"
                except:
                    return "Neither"
            return "IPv4"
            
        elif ":" in queryIP:
            arr = queryIP.split(":")
            if len(arr) != 8:
                return "Neither"
            for i in arr:
                if not (1<=len(i)<=4):
                    return "Neither"
                try:
                    c = int(i,16)
                except:
                    return "Neither"
            return "IPv6"
        return "Neither"