class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = math.inf
        for number in nums:
            if number < min:
                min = number
        return min