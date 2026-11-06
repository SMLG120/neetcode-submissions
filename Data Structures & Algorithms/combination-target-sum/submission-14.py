class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, current, total):
            if total == target:
                res.append(current.copy())
                return
            if total > target or i == len(nums):
                return
            current.append(nums[i])
            backtrack(i, current, total + nums[i])
            current.pop()
            backtrack(i + 1, current, total)
        
        backtrack(0, [], 0)
        return res

        