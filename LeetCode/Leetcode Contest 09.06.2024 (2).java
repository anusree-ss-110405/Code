// You are using Java
class Solution {
    public int sumAfterKSeconds(int n, int k) {
        final int MOD = 1000000007;
        int[] a = new int[n];

        // Initialize the array with 1s
        for (int i = 0; i < n; i++) {
            a[i] = 1;
        }

        // Perform the updates for k seconds
        for (int second = 0; second < k; second++) {
            for (int i = 1; i < n; i++) {
                a[i] = (a[i] + a[i - 1]) % MOD;
            }
        }

        return a[n - 1];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int n = 4;
        int k = 5;
        System.out.println(sol.sumAfterKSeconds(n, k));  // Output should be 5
    }
}
