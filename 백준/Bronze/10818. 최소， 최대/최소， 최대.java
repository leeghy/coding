import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		int N = scanner.nextInt();
		
		int max = -1000000;
		int min = 1000000;

		for (int i = 0; i < N; i++) {
			int x = scanner.nextInt();
			if (x > max) {
				max = x;
			}
			if (x < min) {
				min = x;
			}
		}
		
		System.out.printf("%d %d", min, max);

		scanner.close();

	}
}