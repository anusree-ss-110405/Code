package GeeksforGeeks;
//{ Driver Code Starts
// Initial Template for Java

/*
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine().trim());
        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine().trim());
            String[] str = br.readLine().trim().split(" ");
            int[] array = new int[n - 1];
            for (int i = 0; i < n - 1; i++) {
                array[i] = Integer.parseInt(str[i]);
            }
            Solution sln = new Solution();
            System.out.println(sln.missingNumber(array, n));
        }
    }
}
*/
// } Driver Code Ends


// User function Template for Java

import java.util.Arrays;

class Solution {
    int missingNumber(int array[], int n) {
        Arrays.sort(array);
        int sum=(n*(n+1))/2;
        int arrsum=0;
        for(int i=0;i<n-1;i++)
        {
            arrsum+=array[i];
        }
        int res=sum-arrsum;
        return res;
    }
}