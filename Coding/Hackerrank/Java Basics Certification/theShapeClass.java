import java.util.*;

class Shape
{
    protected int length;
    protected int breadth;
    public Shape(int l,int b)
    {
        this.length=l;
        this.breadth=b;
    }
    public void area()
    {
        System.out.println(length+" "+breadth);
    }
}
class Rectangle extends Shape{
    Rectangle (int l,int b)
    {
        super(l,b);
    }
    @Override
    public void area()
    {
        System.out.println(length*breadth);
    }
}
public class theShapeClass {
    public static void main(String args[] ) throws Exception {
        Scanner sc = new Scanner(System.in);
        int l = sc.nextInt();
        int b = sc.nextInt();

        Shape shape = new Shape(l,b);
        shape.area();

        Shape rectangle = new Rectangle(l,b);
        rectangle.area();

        sc.close();
    }
}