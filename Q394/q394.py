class Solution:
    def decodeString(self, s: str) -> str:
        numstack = []
        charstack = []
        output = ''

        cur_num = ''
        for i in s:
            if i.isdigit():
                cur_num += i
            elif i=="[":
                numstack.append(int(cur_num))
                cur_num = ''
                charstack.append('')
            elif i=="]":
                new_chars = numstack.pop() * charstack.pop()
                if len(charstack) > 0:
                    charstack[-1] += new_chars
                else:
                    output += new_chars
            else:
                if len(charstack) > 0:
                    charstack[-1] += i
                else:
                    output += i
        return output

x = Solution()
print( x.decodeString("2[abc]3[cd]ef") )