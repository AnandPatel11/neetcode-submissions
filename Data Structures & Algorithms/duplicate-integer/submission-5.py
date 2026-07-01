class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr2 = {}
        for i in nums:
            if i in arr2:
                return True
            else:
                arr2[i] = 1

        return False