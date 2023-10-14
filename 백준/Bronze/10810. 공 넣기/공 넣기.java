import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		int N = scanner.nextInt();
		int M = scanner.nextInt();

		int arr[] = new int[N];

		for (int i = 0; i < N; i++) {
			arr[i] = 0;
		}

		for (int l = 0; l < M; l++) {
			int i = scanner.nextInt();
			int j = scanner.nextInt();
			int k = scanner.nextInt();

			for (int q = i - 1; q < j; q++) {
				arr[q] = k;
			}
		}

		for (int i = 0; i < N; i++) {
			System.out.print(arr[i] + " ");
		}

		scanner.close();

	}
}