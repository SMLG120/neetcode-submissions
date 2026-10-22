from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @lru_cache(None)
        def dfs(sum):
            if sum == 0:
                return 0
            res = 1e9
            for c in coins:
                if sum - c >= 0:
                    kiet = 1 + dfs(sum - c)
                    res = min(res, kiet)
            return res
        
        minCount = dfs(amount)
        return minCount if minCount < 1e9 else -1