import java.util.*;
public class nthFibonacciNumber {
	public static int F(int n){
		if(n==0)
		return 0;
		else if(n==1)
		return 1;
		return F(n-1)+F(n-2);
	}
	public static void main(String[] args) {
		Scanner in=new Scanner(System.in);
		System.out.println(F(in.nextInt()));
        in.close();
	}
}

