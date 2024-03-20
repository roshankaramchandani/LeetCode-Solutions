class Solution {
    private Map<Integer, Integer> memo = new HashMap<>();

    public int tribonacci(int n) {
        if (this.memo.containsKey(n)) {
            return this.memo.get(n);
        }
        if (n == 0) {
            return 0;
        }
        if (n <= 2) {
            return 1;
        }

        int ans = this.tribonacci(n - 1) + this.tribonacci(n - 2) + this.tribonacci(n - 3);
        this.memo.put(n, ans);
        return ans;
    }
}