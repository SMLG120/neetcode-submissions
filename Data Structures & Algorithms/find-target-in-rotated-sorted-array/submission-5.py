class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]: # find our corresponding target
                return m
            
            if nums[l] <= nums[m]: # left side
                if target > nums[m] or target < nums[l]:
                    l = m + 1 # go right side and reset l
                else:
                    r = m - 1 # stay left side and reset r
            else: # right side
                if target < nums[m] or target > nums[r]:
                    r = m - 1 # go left side and reset r
                else:
                    l = m + 1 # stay right side and reset l
        return -1


