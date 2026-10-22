class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1] * n

        for i in range(n):
            for prev in range(0, i):
                if nums[i] > nums[prev]:
                    lis[i] = max(lis[i], lis[prev] + 1)
        return max(lis)
