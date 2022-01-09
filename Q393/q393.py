class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        index = 0
        while index < len(data):
            cur_byte = bin(data[index])[2:].zfill(8)
            if cur_byte[0] == "0":
                index += 1
                continue
            if "0" not in cur_byte:
                return False
            leading_ones = cur_byte.index("0")
            if leading_ones not in (2,3,4):
                return False
            for i in range(1,leading_ones):
                if i+index >= len(data):
                    return False
                ahead_byte = bin(data[i+index])[2:].zfill(8)
                if ahead_byte[:2] != "10":
                    return False
            index += leading_ones
        return True