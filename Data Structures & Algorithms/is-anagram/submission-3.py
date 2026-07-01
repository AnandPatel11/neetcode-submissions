class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        smap = {}
        tmap = {}

        for i in range(len(s)):
            if s[i] in smap:
                smap[s[i]] += 1
            else:
                smap[s[i]] = 1
            if t[i] in tmap:
                tmap[t[i]] += 1
            else:
                tmap[t[i]] = 1
        
        return smap == tmap