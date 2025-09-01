import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        if num < 0:
            return False
        if num == 0:
            return True
        new = 0

        while num > 0:
            right = num % 10
            new = new*10 + right
            num = (num)//10

        print(x, new)
        return x==new

sol = Solution()

res = sol.isPalindrome(10011001)
print(res)
