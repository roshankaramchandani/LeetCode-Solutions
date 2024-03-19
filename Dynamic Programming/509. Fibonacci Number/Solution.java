class Solution {
    private Map<Integer, Integer> memo = new HashMap<>();

    public int fib(int n) {
        if (this.memo.containsKey(n)) {
            return this.memo.get(n);
        }
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }

        int ans = this.fib(n - 1) + this.fib(n - 2);
        this.memo.put(n, ans);
        return ans;
    }
}