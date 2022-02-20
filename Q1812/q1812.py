class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = ord(coordinates[0]) - 97
        y = int(coordinates[1]) - 1
        return x%2 != y%2