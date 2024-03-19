class Solution {
    public int minPathSum(int[][] grid) {
        int r = grid.length;
        int c = grid[0].length;
        for (int i = r - 1; i >= 0; i--) {
            for (int j = c - 1; j >= 0; j--) {
                int curr = grid[i][j];
                if (i != r - 1 && j != c - 1) {
                    grid[i][j] = curr + Math.min(grid[i + 1][j], grid[i][j + 1]);
                } else if (i != r - 1) {
                    grid[i][j] = curr + grid[i + 1][j];
                } else if (j != c - 1) {
                    grid[i][j] = curr + grid[i][j + 1];
                }
            }
        }
        return grid[0][0];
    }
}