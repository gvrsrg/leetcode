class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = len(nums)
        if (l <= 1):
            return l
        curr = nums[0]
        next = nums[1]
        i = 0
        while i <= l - 2:
            curr = nums[i]
            next = nums[i + 1]
            while ((curr == next) and (i + 1 <= l - 1)):
                nums.pop(i + 1)
                l = len(nums)
                if (i + 1 < l - 1):
                    next = nums[i + 1]
                else:
                    next += 1
                    continue
            i += 1

        l = len(nums)
        return l


sol = Solution()

nums = [1,1,1]
res = sol.removeDuplicates(nums)
print(res)

