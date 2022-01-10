class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b = map(int,num1[:-1].split("+"))
        c, d = map(int,num2[:-1].split("+"))
        first_num = (a*c) - (b*d)
        second_num = (a*d) + (b*c)
        return f"{first_num}+{second_num}i"
        

x = Solution()
print( x.complexNumberMultiply("1+1i", "1+1i") )