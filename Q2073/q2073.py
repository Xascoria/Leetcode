from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        req_time = tickets[k]
        output = 0
        for i in range(k+1):
            output += min(tickets[i], req_time)
        for i in range(k+1,len(tickets)):
            output += min(tickets[i], req_time-1)
        return output