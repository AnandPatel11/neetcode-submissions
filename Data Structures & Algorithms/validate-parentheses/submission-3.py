class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {'(':')', '{':'}', '[':']'}


        for i in range(len(s)):
            if s[i] in hmap:
                stack.append(s[i])
            else:
                print(s[i])
                if stack and (hmap[stack[-1]] == s[i]):
                    stack.pop()
                else:
                    return False

        return not stack