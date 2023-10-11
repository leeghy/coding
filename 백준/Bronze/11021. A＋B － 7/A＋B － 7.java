import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		int T = scanner.nextInt();
		int arr[] = new int[T];
		for (int i = 0; i < T; i++) {
			int a = scanner.nextInt();
			int b = scanner.nextInt();

			arr[i] = a + b;
		}

		for (int i = 0; i < T; i++) {
			System.out.printf("Case #%d: %d\n", i + 1, arr[i]);
		}
	}
}