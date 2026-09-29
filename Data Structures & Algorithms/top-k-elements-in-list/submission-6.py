class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        otpt = {}
        for i in nums:
            if i in otpt:
                otpt[i] += 1
            else:
                otpt[i] = 1

        res = [[] for i in range(len(nums)+1)]

        for keys, vals in otpt.items():
            res[vals].append(keys)

        fin = []

        for i in range(len(res) - 1, 0, -1):
            for j in res[i]:
                fin.append(j)
                if len(fin) == k:
                    return fin