class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        first_string = strs[0]
        key = "".join(sorted(first_string))
        d={key:[first_string]}
        #print(d)
        for i in range(1, len(strs)):
            key = "".join(sorted(strs[i]))
            if key not in d:
                d[key] = [strs[i]]
            else:
                d[key].append(strs[i])
        return d.values()