class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pat_arr = []
        index = 0
        while index < len(p)-1:
            if p[index+1] == "*":
                newentry = p[index:index+2]
                if len(pat_arr) > 0 and newentry == pat_arr[-1]:
                    index += 2
                    continue
                pat_arr.append(newentry)
                index += 2
            else:
                pat_arr.append(p[index])
                index+= 1
        if p[-1] != "*":
            pat_arr.append(p[-1])   
        not_processed = [(0,0)]
        while len(not_processed) != 0:
            s_index, p_index = not_processed[0]
            if pat_arr[p_index][0]=="." or s[s_index] == pat_arr[p_index][0]:
                if True:
                    new_out = (s_index+1, p_index+1)
                    if new_out == (len(s),len(pat_arr)):
                        return True
                    if new_out[0] == len(s):
                        if all(len(i)==2 for i in pat_arr[new_out[1]:]):
                            return True
                    if new_out[1] != len(pat_arr) and new_out[0] != len(s):
                        not_processed += [new_out]
                if len(pat_arr[p_index]) == 2:
                    new_out = (s_index+1, p_index)
                    if new_out == (len(s),len(pat_arr)):
                        return True
                    if new_out[0] == len(s):
                        if all(len(i)==2 for i in pat_arr[new_out[1]:]):
                            return True
                    if new_out[1] != len(pat_arr) and new_out[0] != len(s):
                        not_processed += [new_out]
            if len(pat_arr[p_index]) == 2:
                new_out = (s_index, p_index+1)
                if new_out == (len(s),len(pat_arr)):
                    return True
                if new_out[0] == len(s):
                    if all(len(i)==2 for i in pat_arr[new_out[1]:]):
                        return True
                if new_out[1] != len(pat_arr) and new_out[0] != len(s):
                    not_processed += [new_out]
            not_processed.pop(0)
        return False

x = Solution()
print( x.isMatch("aaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*a*a*b") )
