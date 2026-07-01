class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi, i, j = 0, 0, len(heights) - 1
        prod = 0
        while i < j:
            prod = (j-i)*min(heights[i], heights[j])
            if prod > maxi:
                maxi = prod
                print(i, j, maxi)
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1

        return maxi
            