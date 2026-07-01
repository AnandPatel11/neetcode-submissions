class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        arr = [[] for i in range(len(nums) + 1)]
        for i in nums:
            hmap[i] = 1 + hmap.get(i, 0)

        for a, b in hmap.items():
            arr[b].append(a)
        print(len(arr))
        res = []
        for j in range(len(arr)-1, 0, -1):
            for l in arr[j]:
                res.append(l)
                if len(res) == k:
                    return res