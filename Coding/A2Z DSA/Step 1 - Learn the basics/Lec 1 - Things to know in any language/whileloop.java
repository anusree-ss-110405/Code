import java.util.*;
class whileloop {
	
	public static void main(String[] args) {
		Scanner in=new Scanner(System.in);
		int n=in.nextInt();
		int odd=0;
		int even=0;
		int d=0;
		while(n!=0)
		{
			d=n%10;
			if(d%2==0)
			{
				even=even+d;
			}
			else
			{
				odd=odd+d;
			}
			n=n/10;
		}
		System.out.println(even+" "+odd);
		in.close();
	}
}
