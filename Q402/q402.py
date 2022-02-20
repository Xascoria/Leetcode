class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k: return '0'

        prev = num
        output = ''
        removed = 0
        while removed != k:
            print('what')
            output = ''
            for i in range(len(prev)-1):
                if prev[i] > prev[i+1]:
                    removed += 1
                    if removed == k:
                        output += prev[i+1:]
                        break
                else:
                    output += prev[i]
            else: output += prev[-1]
            #print(output,removed)
            if removed == k:
                break
            prev = output
            output = ''
            for i in range(len(prev)-1,0,-1):
                if prev[i] >= prev[i-1]:
                    removed += 1
                    if removed == k:
                        output = prev[:i] + output
                        break
                else:
                    output = prev[i] + output
            else: output = prev[0] + output
            prev = output
            print(output)
        k = output.lstrip('0')
        if not k:
            return '0'
        return k

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        removed = 0
        for i in range(len(num)):
            if stack:
                while stack and removed != k:
                    if stack[-1] > num[i]:
                        stack.pop()
                        removed += 1
                    else:
                        break
                stack.append(num[i])
            else:
                stack.append(num[i])
            if removed == k:
                stack += list(num[i+1:])
                break
        if removed != k:
            #print(stack)
            stack = stack[:-k+removed]
            #print(stack)
        ans =  ''.join(stack).lstrip('0')
        if not ans:
            return '0'
        return ans

x = Solution()
print( x.removeKdigits("1173", k = 2) )