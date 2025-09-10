class Solution:
    def climbStairs(self, stairs: int, steps: list[int]) -> int:

        if len(steps) == 0:
            return 1
        # validSteps is a list, where validSteps[i] = list of steps, that are not greater then i

        validSteps = [[s for s in steps if s <= i] for i in range(stairs + 1)]

        stepByStep = {0:1}

        ways = 0

        min_step = min(steps)
        if min_step > stairs:
            return 0
        else:
            for i in range(1, min_step):
                stepByStep[i] = 0
            stepByStep[min_step] = 1
            ways += 1

        for i in range(min_step + 1, stairs + 1):
            currentValidSteps = validSteps[i]
            ways = 0
            for j in range(len(currentValidSteps)):
                step = currentValidSteps[j]
                if step > i:
                    break
                ways += stepByStep[i-step]

            stepByStep[i] = ways

        print(validSteps, stepByStep)

        return ways

sol = Solution()

stairs = 13
steps = [1, 2]

print(stairs, sol.climbStairs(stairs, steps))