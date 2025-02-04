import java.util.Scanner;

public class ChessGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int n = scanner.nextInt();
        String outcomes = scanner.next();
        
        int antonWins = 0;
        int danikWins = 0;
        
        for (int i = 0; i < n; i++) {
            if (outcomes.charAt(i) == 'A') {
                antonWins++;
            } else {
                danikWins++;
            }
        }
        
        if (antonWins > danikWins) {
            System.out.println("Anton");
        } else if (danikWins > antonWins) {
            System.out.println("Danik");
        } else {
            System.out.println("Friendship");
        }
        
        scanner.close();
    }
}