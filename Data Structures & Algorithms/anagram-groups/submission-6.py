class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for i in strs:
            srtd = ''.join(sorted(i))
            if srtd in hmap:
                hmap[srtd].append(i)
            else:
                hmap[srtd] = [i]

        otpt = []

        for j in hmap.values():
            otpt.append(j)

        return otpt