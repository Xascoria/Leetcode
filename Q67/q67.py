class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = sorted([a,b],key=len)
        carryover = 0
        output = []
        for i in range(len(a)):
            new_digit = int(a[-i-1]) + int(b[-i-1]) + carryover
            output.append(new_digit % 2)
            carryover = new_digit >= 2
        for j in range(i+1,len(b)):
            new_digit = int(b[-j-1]) + carryover
            output.append(new_digit % 2)
            carryover = new_digit == 2
        if carryover: output += [1]
        return "".join(map(str,output[::-1]))

x = Solution()
a = "110"
b = "1011"

res = x.addBinary(a,b)
print(res)
print(bin(int(a,2)+int(b,2)))