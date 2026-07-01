class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        
        for i in nums:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1
                
            if(hmap[i]>1):
                return True

        return False
        