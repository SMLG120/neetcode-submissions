class Solution {
    public int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        for (int i = coins.length - 1; i >= 0; i--){
            for(int a = 1; a <= amount; a++){
                if (a >= coins[i]){
                    dp[a] += dp[a - coins[i]];
                } else {
                    dp[a] += 0;
                }
            }
        }
        return dp[amount];
    }
}
