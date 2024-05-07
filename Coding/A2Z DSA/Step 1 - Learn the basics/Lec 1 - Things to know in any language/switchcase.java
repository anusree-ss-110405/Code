import java.util.*;
public class switchcase {
    public static void main (String[] args){
        Scanner in=new Scanner(System.in);
        int n=in.nextInt();
        double arr[]=new double[n];
        for(int i=0;i<n;i++){
            arr[i]=in.nextDouble();
        }
        System.out.print(areaSwitchCase(n, arr));
        in.close();
    }
    public static double areaSwitchCase(int ch, double []a) {
        switch(ch)
        {
            case 2:
                return(a[0]*a[1]);
            case 1: 
                return(Math.PI*a[0]*a[0]);
        }
        return -1;
    }
}