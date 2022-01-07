class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = [i for i in path.split("/") if i]
        path_stack = []
        for i in arr:
            if i == "..":
                if path_stack:
                    path_stack.pop()
            elif i == ".":
                continue
            else:
                path_stack.append(i)
        return "/" + "/".join(path_stack)

x = Solution()
print( x.simplifyPath("../home//foo/") )