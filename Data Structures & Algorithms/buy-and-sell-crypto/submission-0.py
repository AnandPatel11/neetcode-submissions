class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        l = 0
        for r in range(1, len(prices)):
            diff = prices[r] - prices[l]
            if diff < 0:
                l = r
                continue
            maxi = max(maxi, diff)

        return maxi
            