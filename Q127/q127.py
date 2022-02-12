from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:


        masterdict = {}

        for word in wordList:
            for i in range(len(word)):
                arr = list(word)
                arr[i] = "*"
                nw = ''.join(arr)
                if nw not in masterdict:
                    masterdict[nw] = set()
                masterdict[nw].add(word)

        for i in range(len(beginWord)):
            arr2 = list(beginWord)
            arr2[i] = "*"
            nw2 = ''.join(arr2)
            if nw2 not in masterdict:
                masterdict[nw2] = set()
            masterdict[nw2].add(beginWord)

        # for i in masterdict:
        #     print(i, masterdict[i])

        visited_word = {beginWord}
        to_be_processed = [ ( beginWord, 1 )]
        req_lang = len(wordList) + (beginWord not in wordList)

        #print(to_be_processed)
        while len(visited_word) != req_lang and len(to_be_processed):
            start, step = to_be_processed.pop(0)

            for i in range(len(start)):
                arr = list(start)
                arr[i] = "*"
                for next_word in masterdict[''.join(arr)]:
                    if next_word not in visited_word:
                        to_be_processed.append( (next_word, step+1) )
                        visited_word.add(next_word)
            if endWord in visited_word:
                return step+1
            #print(to_be_processed)
            #print(visited_word)

        return 0

x = Solution()
a="qa"
b="sq"
c=["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to",
"ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb",
"yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me",
"mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
a="hit"
b="cog"
c=["hot","dot","dog","lot","log","cog"]
print( x.ladderLength(a,b,c) )