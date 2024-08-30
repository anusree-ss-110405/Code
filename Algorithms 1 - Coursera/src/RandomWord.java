import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomWord {
    public static void main(String[] args) {
        String champion = null;
        int count = 0;

        while (!StdIn.isEmpty()) {
            String currentWord = StdIn.readString();
            count++;

            // Select the current word with probability 1/count
            if (StdRandom.uniformInt(count) == 0) {
                champion = currentWord;
            }
        }

        if (champion != null) {
            StdOut.println(champion);
        }
    }
}
