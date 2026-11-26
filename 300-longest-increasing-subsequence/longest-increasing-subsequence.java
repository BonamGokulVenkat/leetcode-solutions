class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[][] dp = new int[n][n + 1];
        for (int[] row : dp) java.util.Arrays.fill(row, -1);
        return dfs(0, -1, nums, dp, n);
    }

    private int dfs(int idx, int pidx, int[] nums, int[][] dp, int n) {
        if (idx == n) return 0;
        if (dp[idx][pidx + 1] != -1) return dp[idx][pidx + 1];

        int take = 0;
        if (pidx == -1 || nums[idx] > nums[pidx]) {
            take = 1 + dfs(idx + 1, idx, nums, dp, n);
        }
        int notTake = dfs(idx + 1, pidx, nums, dp, n);

        return dp[idx][pidx + 1] = Math.max(take, notTake);
    }
}