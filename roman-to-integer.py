class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I": 1,
                  "V": 5,
                  "X": 10,
                  "L": 50,
                  "C": 100,
                  "D": 500,
                  "M": 1000}
        arab = 0
        prev = 0
        for r in s[::-1]:
            curr = romans[r]
            if curr < prev:
                arab -= curr
            else:
                arab += curr
            prev = curr
        return arab

sol = Solution()

print(sol.romanToInt("MCMLXXVII"))