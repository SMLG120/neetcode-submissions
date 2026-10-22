class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # think of start array = [3,4,5,1,2] with target = 4
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            # left portion array
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1 # check right side
                else:
                    r = m - 1# check left side
            # right portion array
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1 # check left side
                else:
                    l = m + 1 # check right side
        return -1
                
