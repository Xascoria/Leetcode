class Bitset:

    def __init__(self, size: int):
        self.bitset = [0] * size
        self.negative_bitset = [1] * size
        self.one_count = 0

    def fix(self, idx: int) -> None:
        if self.bitset[idx] == 0:
            self.one_count += 1
        self.bitset[idx] = 1
        self.negative_bitset[idx] = 0

    def unfix(self, idx: int) -> None:
        if self.bitset[idx] == 1:
            self.one_count -= 1
        self.bitset[idx] = 0
        self.negative_bitset[idx] = 1

    def flip(self) -> None:
        self.one_count = len(self.bitset) - self.one_count
        self.bitset, self.negative_bitset = self.negative_bitset, self.bitset

    def all(self) -> bool:
        return self.one_count == len(self.bitset)

    def one(self) -> bool:
        return self.one_count > 0

    def count(self) -> int:
        return self.one_count

    def toString(self) -> str:
        return ''.join(map(str,self.bitset))


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()