class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recursion(current_str):
            if len(current_str) == n*2:
                return [current_str]
            output = []
            a = current_str.count("(")
            b = current_str.count(")")
            if a > b:
                output += recursion(current_str+")")
            if a < n:
                output += recursion(current_str+"(")
            return output
        return recursion("")