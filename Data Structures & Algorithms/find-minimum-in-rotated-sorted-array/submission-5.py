class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            # edge case when array already sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            # get middle index
            m = (l + r) // 2
            # Compute min
            res = min(res, nums[m])

            if nums[m] >= nums[l]: # if left side sorted
                l = m + 1 # search right
            else: # if right side sorted
                r = m - 1 # search left
        return res



