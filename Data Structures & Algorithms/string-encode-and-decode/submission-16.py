class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        a = []
        b = 0
        i = int(0)
        while i < len(s):
            if s[i].isdigit():
                b = (b*10) + (ord(s[i])-ord('0'))
                i = i + 1
            elif s[i] == '#':
                a.append(s[i+1: (b+i+1)])
                i = (b+i+1)
                b=0
            
            #print(a)
            #print(i, b)



        return a

