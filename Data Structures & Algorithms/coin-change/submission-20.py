class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            res = 1e9
            for c in coins:
                if amount - c >= 0:
                    res = min(res, dfs(amount - c) + 1)
            memo[amount] = res
            return res
        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins
            