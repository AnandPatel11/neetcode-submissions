class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        mini = nums[l]
        while l<=r:
            m = (r+l)//2
            mini = min(mini, nums[m])
            if nums[l] <= nums[r]:
                mini = min(mini, nums[l])
                break
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m -1

        return mini