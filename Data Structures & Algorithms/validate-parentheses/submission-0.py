class Solution:
    def isValid(self, s: str) -> bool:
        abc = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                abc.append(i)
            elif i == ")" and len(abc) != 0 and abc[-1] == "(":
                abc.pop()
            elif i == "]" and len(abc) != 0 and abc[-1] == "[":
                abc.pop()
            elif i == "}" and len(abc) != 0 and abc[-1] == "{":
                abc.pop()           
            else:
                return False
        if len(abc) == 0:
            return True
        else:
            return False