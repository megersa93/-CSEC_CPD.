import java.util.Arrays;
import java.util.Scanner;

public class ToyBox {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
    
        int n = scanner.nextInt();
        int[] heights = new int[n];

        for (int i = 0; i < n; i++) {
            heights[i] = scanner.nextInt();
        }

        Arrays.sort(heights);
        for (int i = 0; i < n; i++) {
            System.out.print(heights[i] + (i < n - 1 ? " " : ""));
        }
        
        scanner.close();
    }
}
