import java.util.*;
public class FindCharacterCase {
    
    public static void main(String[] args) {
       Scanner in=new Scanner(System.in);
       char c=in.next().charAt(0);
       if(c>=65&& c<=90)
       {
           System.out.print(1);
       }
       else if(c>=97&&c<=122)
       {
           System.out.print(0);
       }
       else
       {
           System.out.print(-1);
       }
    in.close();
    }
}