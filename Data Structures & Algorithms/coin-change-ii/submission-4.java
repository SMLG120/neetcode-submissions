class Solution {
    public int change(int amount, int[] coins) {
        int n = coins.length;
        Arrays.sort(coins);
        int[][] dp = new int[n + 1][amount + 1];
        for (int i = 0 ; i <= n; i ++){
            dp[i][0] = 1;
        }
        // Loop through coins first from bottom to up
        for(int i = n - 1; i >= 0; i--){
            // Loop from amounts small to big left to right
            for (int a = 0; a <= amount; a++){
                // take previous from bottom
                dp[i][a] = dp[i + 1][a];
                if (a >= coins[i]){
                    dp[i][a] += dp[i][a - coins[i]];
                }
            }
        }
        return dp[0][amount];
    }
}
