class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pat_arr = []
        for i in p:
            if i != "*":
                pat_arr.append(i)
            elif len(pat_arr) > 0 and pat_arr[-1] == "*":
                continue
            else:
                pat_arr.append("*")
        
        ## String ptr, pat arr ptr
        #cur_states = {(0,0)}
        cur_indexes = {0}
        for i in pat_arr:
            new_states = set()
            new_indexes = set()
            if i == "?":
                for j in cur_indexes:
                    if j != len(s): 
                        new_indexes.add(j+1)
                    #new_states.add( (j[0]+1,j[1]+1) )
            elif i == "*":
                for j in cur_indexes:
                    for k in range(j, len(s)+1):
                        #new_states.add( (k, j[1]+1) )
                        new_indexes.add(k)
            else:
                for j in cur_indexes:
                    #if s[j[0]] == i:
                    #    new_states.add( (j[0]+1, j[1]+1) )
                    if j != len(s) and i==s[j]:
                        new_indexes.add(j+1)
            # if len(new_states) == 0:
            #     return False
            # if (len(s),len(pat_arr)) in new_states:
            #     return True
            cur_indexes = new_indexes
            #print(new_indexes)
        return len(s) in cur_indexes
        return False

x = Solution()
print(x.isMatch("adceb","*a*b"))