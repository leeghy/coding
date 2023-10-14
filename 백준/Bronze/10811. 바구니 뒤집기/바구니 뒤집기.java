import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Main m = new Main();
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

			m.reverse(arr, i, j);
		}

		for (int i = 0; i < N; i++) {
			System.out.print(arr[i] + " ");
		}

		scanner.close();

	}

	public void reverse(int arr[], int i, int j) {
		int tmp[] = new int[j - i + 1];

		int n = 0;
		for (int l = j - 1; l >= i - 1; l--) {
			tmp[n] = arr[l];
			n++;
		}

		int m = 0;
		for (int l = i - 1; l < j; l++) {
			arr[l] = tmp[m];
			m++;
		}

	}
}