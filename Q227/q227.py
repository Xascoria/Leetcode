class Solution:
    def calculate(self, s: str) -> int:
        numstack = []
        opstack = ["+"]
        curstr = ""
        for i in s:
            if i in " +-*/":
                if curstr:
                    if opstack[-1] == "*":
                        new_val = numstack[-1] * int(curstr) 
                        numstack.pop()
                        opstack.pop()
                    elif opstack[-1] == "/":
                        new_val = numstack[-1] // int(curstr) 
                        numstack.pop()
                        opstack.pop()
                    else: 
                        new_val = int(curstr) 
                    numstack.append(new_val)
                    curstr = ""
                if i!=" ":
                    opstack += [i]
            else:
                curstr += i
        if curstr: 
            if opstack[-1] == "*":
                new_val = numstack[-1] * int(curstr) 
                numstack.pop()
                opstack.pop()
            elif opstack[-1] == "/":
                new_val = numstack[-1] // int(curstr) 
                numstack.pop()
                opstack.pop()
            else: 
                new_val = int(curstr) 
            numstack.append(new_val)
        
        out = 0
        for i,j in zip(opstack,numstack):
            if i == "+":
                out += j
            else:
                out -= j
        return out
            
        # while len(numstack) != 1:
        #     z=[]
        #     if "*" in opstack: 
        #         z += [opstack.index("*")]
        #     if "/" in opstack: 
        #         z += [opstack.index("/")] 
        #     if len(z)==0:
        #         curop = 0
        #     else:
        #         curop = min(z)
            
                
        #     trueoper = opstack[curop]
        #     if trueoper == "+":
        #         new_val = numstack[curop] + numstack[curop+1]
        #     elif trueoper == "-":
        #         new_val = numstack[curop] - numstack[curop+1]
        #     elif trueoper == "*":
        #         new_val = numstack[curop] * numstack[curop+1]
        #     else:
        #         new_val = numstack[curop] // numstack[curop+1]
        #     numstack = numstack[:curop] + [new_val] + numstack[curop+2:]
        #     opstack.pop(curop)
        # return numstack[0]
        
x = Solution()
print(x.calculate("3+2*2"))