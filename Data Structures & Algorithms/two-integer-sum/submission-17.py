class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasBeen ={}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hasBeen:
                return [hasBeen[diff], i]
            hasBeen[num] = i
        return []