class Solution:
    def intToRoman(self, num: int) -> str:
        output = []
        symbol_dict = {1: "I", 5:"V", 10: "X", 50: "L", 100:"C", 500:"D", 1000:"M"}
        cur_place = 1
        while num:
            digit = num % 10
            #print(digit)
            if digit in (4,9):
                output.append( symbol_dict[cur_place] + symbol_dict[(digit+1)*cur_place] )
            elif cur_place < 1000:
                output.append( (symbol_dict[cur_place*5]) * (digit//5) + (symbol_dict[cur_place]) * (digit%5) )  
            else:
                output.append( (symbol_dict[cur_place]) * (digit%5) )
            num //= 10
            cur_place *= 10
        #print(output)
        return ''.join(output[::-1])

x = Solution()
print( x.intToRoman(1798) )