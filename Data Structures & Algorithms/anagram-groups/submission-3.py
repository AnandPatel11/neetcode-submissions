class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for i in strs:
            if ''.join(sorted(i)) in hmap:
                hmap[''.join(sorted(i))].append(i)
            else:
                hmap[''.join(sorted(i))] = [i]

        otpt = []

        for i in hmap.keys():
            otpt.append(hmap[i])

        return otpt