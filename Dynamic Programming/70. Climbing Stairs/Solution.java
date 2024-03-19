class Solution {
    private Map<Integer, Integer> memo = new HashMap<>();

    public int climbStairs(int n) {
        if (memo.containsKey(n)) {
            return memo.get(n);
        }
        if (n == 0) {
            return 1;
        }
        if (n < 0) {
            return 0;
        }

        int ans = this.climbStairs(n - 1) + this.climbStairs(n - 2);
        memo.put(n, ans);
        return ans;
    }
}