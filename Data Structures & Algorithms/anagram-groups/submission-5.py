class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        otpt = defaultdict(list)
        for each in strs:
            count = [0] * 26
            for eachChar in each:
                count[ord(eachChar) - ord('a')] +=1
            otpt[tuple(count)].append(each)

        return list(otpt.values())
