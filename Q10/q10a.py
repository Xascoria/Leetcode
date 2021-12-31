## An abandoned attempt using non-finite state automata

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pat_arr = []
        index = 0
        while index < len(p)-1:
            if p[index+1] == "*":
                pat_arr.append(p[index:index+2])
                index += 2
            else:
                pat_arr.append(p[index])
                index+= 1
        
        if p[-1] != "*":
            pat_arr.append(p[-1])   

        class State:
            def __init__(self) -> None:
                self.is_end_state = False
                self.children = {}

            def __str__(self):
                return str(self.is_end_state) +" "+ str(self.children.keys())

        true_start = start_state = State()
        for i in pat_arr:
            if len(i) == 2:
                news = State()
                news.children[i[0]] = news
                start_state.children[""] = news
            else:
                news = State()
                start_state.children[i] = news
            start_state = news
        if len(i) == 2:
            news = State()
            start_state.children[""] = news
            news.is_end_state = True
        else:
            start_state.is_end_state = True


        

x = Solution()
print( x.isMatch("abc","abc") )



