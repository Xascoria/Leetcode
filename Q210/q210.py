from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        need_req = [set() for _ in range(numCourses)] 
        for i, j in prerequisites:
            need_req[i].add(j)
        if 0 not in [len(i) for i in need_req]:
            return []
        order = []
        solved = [False] * numCourses
        while True:
            iteration_change = False
            new_added = []
            for i, req in enumerate(need_req):
                if not solved[i]:
                    if len(req) == 0:
                        order += [i]
                        new_added += [i]
                        solved[i] = True
                        iteration_change = True
            if sum([len(i)for i in need_req]) == 0: break
            for i, req in enumerate(need_req):
                if not solved[i]:
                    for j in new_added:
                        if j in req:
                            need_req[i].remove(j)
                            iteration_change = True
            if not iteration_change: 
                return []
        return order