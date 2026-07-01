class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        hmap = {}
        for i in strs:
            abc = ''.join(sorted(i))
            if abc in hmap:
                hmap[abc].append(i)
            else:
                hmap[abc] = [i]

        
        return list(hmap.values())