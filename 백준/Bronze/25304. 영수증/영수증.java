import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		int X = scanner.nextInt();
		int N = scanner.nextInt();

		for (int i = 0; i < N; i++) {
			int a = scanner.nextInt();
			int b = scanner.nextInt();

			X -= a * b;
		}
		
		if (X == 0) System.out.println("Yes");
		else System.out.println("No");
		
		scanner.close();
	}
}
