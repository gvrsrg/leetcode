class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        curr_max, max_so_far = nums[0], float('-inf')
        for c in nums:
            curr_max = max(c, curr_max + c)
            max_so_far = max(max_so_far, curr_max)
            print(f'c: {c}, curr_max: {curr_max}, max_so_far: {max_so_far}')
        return max_so_far


sol = Solution()

nums = [-2,-1,-3,4,-1,2,1,-5,6]
print(sol.maxSubArray(nums))