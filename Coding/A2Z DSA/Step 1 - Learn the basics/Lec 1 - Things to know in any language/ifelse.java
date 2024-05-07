import java.util.*;
public class ifelse {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        int a=in.nextInt();
        int b=in.nextInt();
        String s=compareIfElse(a, b);
        System.out.print(s);
        in.close();
    }
    public static String compareIfElse(int a, int b) {
        if(a>b)
        return ("greater");
        else if(a<b)
        return ("smaller");
        else
        return ("equal");
       
    }
}