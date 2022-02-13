class Solution:
    def reformatDate(self, date: str) -> str:
        d,m,y = date.split()
        a = ('',"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec").index(m)
        return y+'-'+f'{a:02d}-{int(d[:-2]):02d}'