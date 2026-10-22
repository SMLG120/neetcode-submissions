class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        if (n == 0){
            return 0;
        }
        if (n == 1){
            return cost[0];
        }

        int prev0 = cost[0];
        int prev1 = cost[1];

        for(int i = 2 ; i < n; i++){
            int current = cost[i] + Math.min(prev0, prev1);
            prev0 = prev1;
            prev1 = current;
        }

        return Math.min(prev0, prev1);
    }
}
