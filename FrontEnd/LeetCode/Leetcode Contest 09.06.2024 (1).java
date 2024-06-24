class Solution {
    public int numberOfChild(int n, int k) {
        // Initialize the position of the ball and the direction of passing
        int position = 0;
        boolean directionRight = true; // true means moving to the right, false means moving to the left

        // Iterate for k seconds
        for (int i = 0; i < k; i++) {
            if (directionRight) {
                position++;
                if (position == n - 1) {
                    directionRight = false;
                }
            } else {
                position--;
                if (position == 0) {
                    directionRight = true;
                }
            }
        }

        return position;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int n = 3;
        int k = 5;
        System.out.println(sol.numberOfChild(n, k)); // Output should be 1
    }
}
