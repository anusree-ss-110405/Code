// Find First and Last Position of Element in Sorted Array
public class searchRange {
    public static int[] searchinRange(int []arr, int x) {
        // Write your code here.
        int a[]=new int[2];
        // first position
        for(int i=0;i<arr.length;i++){
            if(arr[i]==x){
                a[0]=i;
                break;
            }else{
                a[0]=-1;
            }
        }
        // last position
        for(int i=arr.length-1;i>=0;i--){
            if(arr[i]==x){
                a[1]=i;
                break;
            }else{
                a[1]=-1;
            }
        }
        return a;
    }
}