class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest = set()
        maxi = 0
        long = 0
        while r < len(s):
            if s[r] not in longest:
                longest.add(s[r])
                long +=1
                r +=1
                #print(longest)
                maxi = max(maxi, long)
            else:
                while s[r] in longest:
                    longest.remove(s[l])
                    l+=1
                    long -=1

        return maxi
