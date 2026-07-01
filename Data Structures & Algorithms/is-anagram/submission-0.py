class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        oppo = {}
        popo = {}

        for i in range(len(s)):
            if s[i] in oppo:
                oppo[s[i]] += 1
            else:
                oppo[s[i]] = 1

            if t[i] in popo:
                popo[t[i]] += 1
            else:
                popo[t[i]] = 1

        return oppo == popo