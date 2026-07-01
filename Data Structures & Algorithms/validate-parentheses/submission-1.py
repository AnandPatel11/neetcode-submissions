class Solution:
    def isValid(self, s: str) -> bool:
        abc = []
        bracks = {")":"(", "}":"{", "]":"["}

        for i in s:
            if i in bracks:
                if abc and abc[-1] == bracks[i]:
                    abc.pop()
                else:
                    return False
            else:
                abc.append(i)

        return True if not abc else False