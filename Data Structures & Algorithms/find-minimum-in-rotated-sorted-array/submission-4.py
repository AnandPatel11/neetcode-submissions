class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, m = 0, len(nums)-1, len(nums)//2
        mini = nums[l]
        while l<=r:
            m = (r+l)//2
            mini = min(mini, nums[m])
            #print(nums[l], nums[m], nums[r], mini)
            if nums[l] <= nums[r]:
                mini = min(mini, nums[l])
                break
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m + -1
            m = (r+l)//2

        return mini