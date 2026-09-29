class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for each in strs:
            sortedEach = ''.join(sorted(each))
            if sortedEach in hmap:
                hmap[sortedEach].append(each)
            else:
                hmap[sortedEach] = [each]
        otpt = []
        for vals in hmap.values():
            otpt.append(vals)

        return otpt
