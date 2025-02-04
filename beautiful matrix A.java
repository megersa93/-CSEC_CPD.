import java.util.Scanner;

public class BeautifulMatrix {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int oneRow = -1;
        int oneCol = -1;
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                int value = scanner.nextInt();
                if (value == 1) {
                    oneRow = i + 1; 
                    oneCol = j + 1; 
                }
            }
        }

        int targetRow = 3;
        int targetCol = 3;
        int rowMoves = Math.abs(oneRow - targetRow);
        int colMoves = Math.abs(oneCol - targetCol);
  
        int totalMoves = rowMoves + colMoves;
        System.out.println(totalMoves);
        
        scanner.close();
    }
}
