class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        start = "({["
        end = ")}]"
        for i in s:
            if i in end and len(stack) == 0:
                return False
            if i in start:
                stack += [end[start.index(i)]]
            else:
                if stack[-1] == i:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        