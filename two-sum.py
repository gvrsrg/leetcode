class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i in range(0, len(nums)):
            if (d.get(target-nums[i], "False") != "False"):
                return [i, d.get(target-nums[i], "False")]
            else:
                d[nums[i]] = i

        return [False, False]

nums = [2,7,11,15]
target=22

sol = Solution(nums,target)
res = sol.twoSum(nums,target)
print(res)
