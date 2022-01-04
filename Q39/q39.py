class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combi_arr =[None] * (target+1)
        for j in candidates:
            if j >= len(combi_arr): continue
            combi_arr[j] = [[j]]
        for i in range(min(candidates), target+1):
            for j in candidates:
                if i-j >= 0:
                    if combi_arr[i] == None: combi_arr[i] = []
                    if combi_arr[i-j] != None:
                        #combi_arr[i] += [[i]]
                    #else:
                        for series in combi_arr[i-j]:
                            combi_arr[i] += [series+[j]]
        if combi_arr[target] == None: return []                            
        return set(tuple(sorted(i))for i in combi_arr[target])
            