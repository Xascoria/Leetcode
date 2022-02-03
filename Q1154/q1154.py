class Solution:
    def dayOfYear(self, date: str) -> int:
        y,m,d = map(int,date.split("-"))
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if y % 4 == 0:
            if y % 100 == 0:
                if y % 400 == 0:
                    days[1] += 1
            else:
                days[1] += 1
        return d + sum(days[:m-1])