class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            # two decisions to make
            #1 include nums[i] to total
            nums[i]
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            # 2 exclude nums[i]
            # first cleanup by removing in decision tree
            cur.pop() # this line will never include the nums[i]
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)

        return res

            

            