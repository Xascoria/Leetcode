class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        sti = "0123456789"
        numarr = [*range(10)]
        cache = {}
        resarr = []
        for index, digit in enumerate(num1[::-1]):
            carry_over = 0
            output = []
            if digit not in cache:
                d1 = numarr[sti.index(digit)]
                for di2 in num2[::-1]:
                    res = d1 * numarr[sti.index(di2)] + carry_over
                    carry_over = res//10
                    output.append(res%10)
                if carry_over:
                    output.append(carry_over)
                cache[digit] = output
            else:
                output = cache[digit]
            resarr += [[0]*index + output]
        ml = len(max(resarr,key=len))
        resarr = [i+[0]*(ml-len(i)) for i in resarr]
        carry_over = 0
        res = []
        for i in zip(*resarr):
            r = sum(i) + carry_over
            res += [r%10]
            carry_over = r//10
        if carry_over:
            res += [carry_over]
        if len(set(res)) == 1  and res[0]==0:
            return"0"
        return "".join(map(str,res[::-1]))


x = Solution()
print( x.multiply("9133","0") )
print(99*99)