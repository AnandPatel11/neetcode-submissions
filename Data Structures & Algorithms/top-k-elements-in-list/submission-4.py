class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        otpt = {}
        for i in nums:
            if i in otpt:
                otpt[i] += 1
            else:
                otpt[i] = 1

        heap = []

        for num in otpt.keys():
            heapq.heappush(heap, (otpt[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res

