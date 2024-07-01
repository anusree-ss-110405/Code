// Java 
class Solution {
    public boolean threeConsecutiveOdds(int[] nums) {
        int n=nums.length;
        if(n>=3)
        {
            for(int i=0;i<n-2;i++)
            {
                int count=0;
                for(int j=i;j<i+3;j++)
                {
                    if(nums[j]%2!=0)
                    {
                        count++;
                    }
                }
                if(count==3)
                {
                    return true;
                }
            }
        }
        return false;
    }
}
