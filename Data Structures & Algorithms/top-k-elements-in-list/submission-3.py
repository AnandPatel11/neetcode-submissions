class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        otpt = {}
        for i in nums:
            if i in otpt:
                otpt[i] += 1
            else:
                otpt[i] = 1

        arr = []

        for key,val in otpt.items():
            arr.append([val, key])

        arr.sort(reverse=True)
        res=[]
        for i in range(k):
            res.append(arr[i][1])


        return res
