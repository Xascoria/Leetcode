class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_dict = {}
        for i in t:
            if i not in count_dict:
                count_dict[i] = 1
            else:
                count_dict[i] += 1
        ptr1 = 0
        ## Loop to the first viable char usable char
        while s[ptr1] not in count_dict:
            ptr1 += 1
            if ptr1 == len(s):
                return ""
        window_dict = {i:0 for i in count_dict}
        window_dict[s[ptr1]] = 1
        def dict_compare():
            for i in count_dict:
                if count_dict[i] > window_dict[i]:
                    return False
            return True
        ## Prepare second pointer to build the window
        ptr2 = ptr1
        if not dict_compare():
            while True:
                ptr2 += 1
                if ptr2 == len(s):
                    return ""
                if s[ptr2] not in window_dict:
                    continue
                window_dict[s[ptr2]] += 1
                if dict_compare(): break
        
        ## Ensure first window is minimum
        while True:
            if s[ptr1] in window_dict:
                if window_dict[s[ptr1]] == count_dict[s[ptr1]]:
                    break
                window_dict[s[ptr1]] -= 1
            ptr1 += 1
        ## First window finished building, time to iterate
        ## Indexes inclusive
        start_index = ptr1
        end_index = ptr2
        length = ptr2 - ptr1 #Actually len-1 but same purpose
        
        while ptr2 < len(s):
            ptr2 += 1
            if ptr2 == len(s):
                break
            if s[ptr2] not in window_dict:
                #ptr2 += 1
                continue
            if s[ptr2] != s[ptr1]:
                window_dict[s[ptr2]] += 1
                #ptr2 += 1
                continue
            #ptr2 += 1
            
            ptr1 += 1
            #print("bt",ptr1, ptr2, s[ptr1:ptr2+1], window_dict)
            while True:
                if s[ptr1] in window_dict:
                    if window_dict[s[ptr1]] == count_dict[s[ptr1]]:
                        break
                    window_dict[s[ptr1]] -= 1
                    # if window_dict[s[ptr1]] == count_dict[s[ptr1]]:
                    #     break
                ptr1 += 1 
            #print("at",ptr1, ptr2, s[ptr1:ptr2+1], window_dict)
            if ptr2 - ptr1 < length:
                start_index = ptr1
                end_index = ptr2
        return s[start_index:end_index+1]

x = Solution()
print( x.minWindow("ADOBECODEBANC","ABC") )