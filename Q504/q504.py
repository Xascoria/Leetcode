class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:return "0"

        s = "-"*(num<0)
        num=abs(num)
        a = []
        while num:
            a.append( str(num%7) )
            num //= 7
        print(a)