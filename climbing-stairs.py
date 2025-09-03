class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3:
            return n
        prev2 = 2
        prev1 = 3
        result = 0
        i = 4
        while i<=n:
            result = prev1+prev2
            prev2, prev1 = prev1, result
            i += 1
        return result


sol = Solution()
for i in range(1,46):
    print(i, sol.climbStairs(i))