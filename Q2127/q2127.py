from typing import List

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        discovery_path = [None] * len(favorite)
        leads_to_binary_stars = {}
        binary_pairing = {}
        chains_to_binary = {}
        dis_pointer = 0

        output = 0
        output_using_binary_star = False
        bin_cluster = {}
        while dis_pointer < len(discovery_path):
            if discovery_path[dis_pointer] != None:
                dis_pointer += 1
                continue
            discovery_path[dis_pointer] = (dis_pointer, 0)
            next_in_line = favorite[dis_pointer]
            step = 1
            while discovery_path[next_in_line] == None:
                discovery_path[next_in_line] = (dis_pointer, step)
                step += 1
                next_in_line = favorite[next_in_line]
            if discovery_path[next_in_line][0] == dis_pointer:
                ## Deadlock/Binary stars discovered
                if discovery_path[next_in_line][1] == step-2:
                    binary_pairing[next_in_line] = favorite[next_in_line]
                    binary_pairing[favorite[next_in_line]] = next_in_line
                    ## Binary that it leads to
                    
                    #print(discovery_path)
                    #print({dis_pointer: discovery_path[next_in_line], next_in_line: 0})
                    chains_to_binary[next_in_line] = {dis_pointer: discovery_path[next_in_line][1], next_in_line: 0}
                    chains_to_binary[favorite[next_in_line]] = { favorite[next_in_line]:0 }

                    a,b = min(next_in_line, favorite[next_in_line]), max(next_in_line, favorite[next_in_line])
                    bin_cluster[(a,b)] = discovery_path[next_in_line][1]+2
                    if output <= discovery_path[next_in_line][1]+2:
                        using_pair = next_in_line
                        output = discovery_path[next_in_line][1]+2
                        output_using_binary_star = True

                    leads_to_binary_stars[dis_pointer] = (True, next_in_line)
                    discovery_path[favorite[next_in_line]] = (favorite[next_in_line], 0)
                    discovery_path[next_in_line] = (next_in_line, 0)
                    leads_to_binary_stars[favorite[next_in_line]] = (True, favorite[next_in_line])
                    leads_to_binary_stars[next_in_line] = (True, next_in_line)
                    
                    #output = max(output, discovery_path[next_in_line][1]+2)
                else:
                    leads_to_binary_stars[dis_pointer] = (False, -1)
                    ## Normal deadlock
                    #output = max(output, step - discovery_path[next_in_line][1])
                    if output < step - discovery_path[next_in_line][1]:
                        output_using_binary_star = False
                        output = step - discovery_path[next_in_line][1]
            else:
                if leads_to_binary_stars[ discovery_path[next_in_line][0] ][0]:
                    bin_star_lead = leads_to_binary_stars[ discovery_path[next_in_line][0] ][1]
                    ## Deal with connection to binary stars
                    #print("Binary star path")
                    #print(bin_star_lead, discovery_path[next_in_line][0], chains_to_binary)
                    org_chain_length = chains_to_binary[ bin_star_lead ][ discovery_path[next_in_line][0] ] 
                    chains_to_binary[ bin_star_lead ][ dis_pointer ] = org_chain_length - discovery_path[next_in_line][1] + step
                    leads_to_binary_stars[ dis_pointer ] = (True, leads_to_binary_stars[ discovery_path[next_in_line][0] ][1])
                    final_length = chains_to_binary[ bin_star_lead ][ dis_pointer ] + 2
                    k = max(chains_to_binary[ binary_pairing[bin_star_lead] ].values())
                    #print("yoes", chains_to_binary[ binary_pairing[bin_star_lead] ])
                    #print( chains_to_binary )
                    a,b = min(bin_star_lead, binary_pairing[bin_star_lead]), max(bin_star_lead, binary_pairing[bin_star_lead])
                    bin_cluster[(a,b)] = max(bin_cluster[(a,b)], final_length+k)
                    if output <= final_length + k:
                        #print("a[[", org_chain_length, discovery_path[next_in_line][1], step, k,discovery_path[next_in_line])
                        using_pair = bin_star_lead
                        output_using_binary_star = True
                        output = final_length + k
                    #output = max(output, final_length + k)
                else:
                    ## Only leads to a normal deadlock
                    leads_to_binary_stars[ dis_pointer ] = (False, -1)
            dis_pointer += 1
        #print(discovery_path)
        #print(binary_pairing)
        #print(leads_to_binary_stars)
        #print(output)

        return max(output, sum(bin_cluster.values()))

x = Solution()             #[0,1,2,3, 4,5,6, 7,8, 9,10,11,12,13,14,15]
print( x.maximumInvitations([8,3,6,2,12,9,9,12,0,11,11, 3, 4,12, 8, 6]) )