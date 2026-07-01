class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, (len(s)-1)

        while i < j:
            print(s[i],s[j])
            if not (s[i].isalpha() or s[i].isdigit()):
                i += 1
                continue

            if not (s[j].isalpha() or s[j].isdigit()):
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1

        return True
            