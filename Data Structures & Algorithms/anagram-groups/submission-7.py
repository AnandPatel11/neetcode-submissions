class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)

        for i in strs:
            counter = [0] * 26
            for j in i:
                counter[ord(j)-ord('a')] += 1
            hmap[tuple(counter)].append(i)

        return list(hmap.values())