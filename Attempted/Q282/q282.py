from typing import List
import itertools
import re

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        arr = [*num]
        output = []
        # if "00" not in num:
        #     for i in itertools.product(['+','-','*',''],repeat = len(arr)-1):
        #         fs = ''.join( j+k for j,k in zip(arr,i) ) + arr[-1]
        #         try:
        #             if eval(fs) == target:
        #                 output.append(fs)
        #         except:pass
        #     return output
        reg = re.compile('\+00|-00|\*00|^00')
        for i in itertools.product(['+','-','*',''],repeat = len(arr)-1):
            fs = ''.join( j+k for j,k in zip(arr,i) ) + arr[-1]
            try:
                if not reg.search(fs) and eval(fs) == target:
                    output.append(fs)
            except:pass
        return output

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        arr = [*num]
        output = []
        if "00" in num:
            for i in itertools.product(['+','-','*',''],repeat = len(arr)-1):
                fs = ''.join( j+k for j,k in zip(arr,i) ) + arr[-1]
                if "00" in fs:
                    if fs[:2]=="00"or "+00" in fs or "-00" in fs or "*00" in fs:
                        continue
                try:
                    if eval(fs) == target:
                        output.append(fs)
                except:pass
            return output
        for i in itertools.product(['+','-','*',''],repeat = len(arr)-1):
            try:
                if eval(fs :=  ''.join( j+k for j,k in zip(arr,i) ) + arr[-1]) == target:
                    output.append(fs)
            except:pass
        return output

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        arr = []
        for i in num:
            arr += [i, " "]
        arr = arr[:-1]
        output = []
        for i in itertools.product(['+','-','*',''],repeat = len(num)-1):
            
            arr[1::2] = i
            fs = ''.join(arr)
            try:
                if eval(fs) == target and not re.search('\+00|-00|\*00|^00',fs):
                    output.append(fs)
            except:pass
        return output

x = Solution()
print( x.addOperators("000",0) )
#print(re.match( r"^00|\+00|-00|\*00", '1+001' ))
print(re.match(r'-00|\+00|\*00|^00','1+00'))
print(re.search(r"\+00|-00|\*00|^00",'1+00'))