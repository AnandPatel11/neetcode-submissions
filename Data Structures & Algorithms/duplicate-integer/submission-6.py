class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = set()
        for i in nums:
            if i in dups:
                return True
            else:
                dups.add(i)

        return False