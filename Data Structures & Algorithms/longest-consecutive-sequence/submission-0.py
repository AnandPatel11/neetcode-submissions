class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        long = 0
        for i in nums:
            if (i-1) not in arr:
                length = 1
                while(i + length) in arr:
                    length += 1
                
                long = max(length, long)

        return long