class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        
        if len(cost) == 1:
            return cost[0]

        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, len(cost)):
            current = cost[i] + min(prev2, prev1)
            prev2 = prev1
            prev1 = current
        
        return min(prev2, prev1)