class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingDouble(e -> e[1]));
        int[] current = intervals[0];
        int ans = 0;
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < current[1]) {
                ans++;
            } else {
                current = intervals[i];
            }
        }
        return ans;
    }
}