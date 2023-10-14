import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		int res[] = new int[42];

		for (int i = 0; i < 42; i++) {
			res[i] = 0;
		}

		for (int i = 0; i < 10; i++) {
			int x = scanner.nextInt();

			int rest = x % 42;
			res[rest]++;
		}

		int result = 0;
		for (int i = 0; i < 42; i++) {
			if (res[i] != 0) {
				result++;
			}
		}

		System.out.println(result);
		
		scanner.close();

	}
}