class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p3 = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums2[p2] > nums1[p1]:
                nums1[p3] = nums2[p2]
                p2 -= 1
            else:
                nums1[p3] = nums1[p1]
                p1 -= 1
            p3 -= 1

        while p2 >= 0:
            nums1[p3] = nums2[p2]
            p2 -= 1
            p3 -= 1


#        if i < m:
#            i += 1
#        else:



sol = Solution()
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# sol.merge(nums1, m, nums2, n)
# print(nums1)
#
# nums1 = [1]
# m = 1
# nums2 = []
# n = 0
# sol.merge(nums1, m, nums2, n)
# print(nums1)
#
nums1 = [0]
m = 0
nums2 = [1]
n = 1
sol.merge(nums1, m, nums2, n)
print(nums1)

# nums1 = [1,2,4,5,6,0]
# m = 5
# nums2 = [3]
# n = 1
# sol.merge(nums1, m, nums2, n)
# print(nums1)
