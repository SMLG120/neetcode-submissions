class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtracking(i, cur, total):
            if target == total:
                res.append(cur.copy())
                return 
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                
                cur.append(nums[j])
                backtracking(j, cur, total + nums[j])
                cur.pop()
        
        backtracking(0, [], 0)

        return res
            
            