class Solution {

    private Map<Integer, Integer> memo = new HashMap<>();

    public int rob(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }
        return Math.max(this.solve(0, nums), this.solve(1, nums));
    }

    private int solve(int idx, int[] nums) {
        if (this.memo.containsKey(idx)) {
            return this.memo.get(idx);
        }
        if (idx >= nums.length - 2) {
            this.memo.put(idx, nums[idx]);
            return nums[idx];
        }

        int max = 0;

        for (int i = idx + 2; i < nums.length; i++) {
            max = Math.max(this.solve(i, nums), max);
        }
        int ans = nums[idx] + max;
        this.memo.put(idx, ans);
        return this.memo.get(idx);
    }
}