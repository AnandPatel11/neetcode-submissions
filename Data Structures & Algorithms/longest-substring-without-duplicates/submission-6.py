class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxi = 0, 0
        charset = set()

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            maxi = max(maxi, len(charset))
        return maxi