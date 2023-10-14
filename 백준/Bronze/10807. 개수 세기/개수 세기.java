import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		int N = scanner.nextInt();
		int arr[] = new int[N];

		for (int i = 0; i < N; i++) {
			int x = scanner.nextInt();
			arr[i] = x;
		}

		int target = scanner.nextInt();

		int n = 0;

		for (int i = 0; i < N; i++) {
			if (arr[i] == target) {
				n++;
			}
		}

		System.out.println(n);

		scanner.close();

	}
}