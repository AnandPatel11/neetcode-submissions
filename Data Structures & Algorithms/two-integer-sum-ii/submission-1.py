class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        summ, i, j = 0, 0, (len(numbers)-1)
        while i < j:
            #print(i, j)
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            

        