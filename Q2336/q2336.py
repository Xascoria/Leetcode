import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.special_set = set()

        self.cur_limit = 1

    def popSmallest(self) -> int:
        if len(self.special_set) == 0:
            output = self.cur_limit
            self.cur_limit += 1
            return output

        smallest = min(self.special_set)
        self.special_set.remove(smallest)
        return smallest
        

    def addBack(self, num: int) -> None:
        if num >= self.cur_limit or num in self.special_set:
            return 

        if num == self.cur_limit - 1:
            self.cur_limit -= 1
            return 

        self.special_set.add(num)
        
        