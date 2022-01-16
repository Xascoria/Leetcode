class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dist_to_left = [0] * len(seats)
        dist_to_right = [0] * len(seats)

        first_left_enc = first_right_enc = False
        cur_left_val = cur_right_val = len(seats)
        for i in range(len(seats)):
            if seats[i] == 1:
                dist_to_left[i] = 0
                cur_left_val = 0
                first_left_enc = True
            else:
                cur_left_val += first_left_enc
                dist_to_left[i] = cur_left_val
            if seats[-1-i] == 1:
                dist_to_right[-1-i] = 0
                cur_right_val = 0
                first_right_enc = True
            else:
                cur_right_val += first_right_enc
                dist_to_right[-1-i] = cur_right_val

        max_dist_arr = [min(i,j) for i,j in zip(dist_to_left, dist_to_right)]
        #max_ind = max_dist_arr.index( max(max_dist_arr) )
    
        return max(max_dist_arr)