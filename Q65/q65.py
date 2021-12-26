class Solution:
    def isNumber(self, s: str) -> bool:
        if len(s) == 0: return False
        start_index = 0
        if s[0] in "+-":
            start_index += 1
            if len(s) == 1: return False
        has_digit_b4 = False
        is_decimal = False
        has_digit_af = False
        while start_index < len(s):
            if s[start_index].lower() == "e":
                if is_decimal and not (has_digit_b4 or has_digit_af):
                    return False
                if not is_decimal and not has_digit_b4:
                    return False
                return self.isInteger(s[start_index+1:])
            elif s[start_index] == ".":
                if is_decimal:
                    return False
                is_decimal = True
            elif s[start_index].isdigit():
                if not is_decimal:
                    has_digit_b4 = True
                else:
                    has_digit_af = True
            else:
                return False
            start_index += 1

        if not is_decimal:
            return has_digit_b4
        
        return has_digit_b4 or has_digit_af

    def isInteger(self, s:str) -> bool:
        if len(s) == 0: return False
        start_index = 0
        if s[0] in "+-":
            start_index += 1
            if len(s) == 1: return False
        while start_index < len(s):
            if not s[start_index].isdigit():
                return False
            start_index += 1
        return True
        
x = Solution()

ts = [".0e7","abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
for i in ts:
    print(x.isNumber(i))