class Solution:
    def minJumps(self, arr: List[int]) -> int:
        ## Format - number:set(index1, index2)
        indexes_dict = {}

        for i,j in enumerate(arr):
            if j not in indexes_dict:
                indexes_dict[j] = set()
            indexes_dict[j].add(i)
            
        numbers_handled = set()
        jump_arr = [float("inf")] * len(arr)
        jump_arr[0] = 0

        numbers_to_be_handled = {arr[0]}
        indexes_to_be_handled = {1}
        step = 1
        while jump_arr[-1] == float("inf"):
            nntbh = set()
            nitbh = set()
            for num in numbers_to_be_handled:
                for index_of_num in indexes_dict[num]:
                    jump_arr[index_of_num] = min(step, jump_arr[index_of_num])
                    if index_of_num != 0 and jump_arr[index_of_num-1] == float("inf"):
                        nitbh.add(index_of_num-1)
                    if index_of_num != len(jump_arr)-1 and jump_arr[index_of_num+1] == float("inf"):
                        nitbh.add(index_of_num+1)

                numbers_handled.add(num)

            for index in indexes_to_be_handled:
                jump_arr[index] = min(step,jump_arr[index])
                if arr[index] not in numbers_handled:
                    nntbh.add(arr[index])
                if jump_arr[index-1] == float("inf"):
                    nitbh.add(index-1)
                if index+1 != len(jump_arr) and jump_arr[index+1] == float("inf"):
                    nitbh.add(index+1)

            numbers_to_be_handled = nntbh
            indexes_to_be_handled = nitbh
            #print(jump_arr)

            step += 1
    
        return jump_arr[-1]