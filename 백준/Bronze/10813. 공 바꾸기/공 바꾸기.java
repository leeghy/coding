import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		int N = scanner.nextInt();
		int M = scanner.nextInt();

		int arr[] = new int[N];

		for (int i = 0; i < N; i++) {
			arr[i] = i + 1;
		}

		for (int l = 0; l < M; l++) {
			int i = scanner.nextInt();
			int j = scanner.nextInt();
			int tmp = 0;

			tmp = arr[i - 1];
			arr[i - 1] = arr[j - 1];
			arr[j - 1] = tmp;
		}

		for (int i = 0; i < N; i++) {
			System.out.print(arr[i] + " ");
		}

		scanner.close();

	}
}