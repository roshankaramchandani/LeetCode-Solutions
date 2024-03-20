class Solution {

    private Map<Integer, Integer> memo = new HashMap<>();

    public int minCostClimbingStairs(int[] cost) {
        return Math.min(this.solve(0, cost), this.solve(1, cost));
    }

    private int solve(int idx, int[] cost) {
        if (this.memo.containsKey(idx)) {
            return this.memo.get(idx);
        }
        if (idx == cost.length) {
            return 0;
        }
        if (idx == cost.length - 1) {
            this.memo.put(idx, cost[idx]);
            return cost[idx];
        }

        int oneStep = this.solve(idx + 1, cost);
        int twoStep = this.solve(idx + 2, cost);
        int ans = Math.min(oneStep, twoStep);
        this.memo.put(idx, cost[idx] + ans);
        return this.memo.get(idx);
    }
}