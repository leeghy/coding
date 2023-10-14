import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		int arr[] = new int[9];

		for (int i = 0; i < 9; i++) {
			arr[i] = scanner.nextInt();
		}

		int max = 0;
		int index = 0;
		for (int i = 0; i < 9; i++) {
			if (arr[i] > max) {
				max = arr[i];
				index = i;
			}
		}

		System.out.println(max + "\n" + (index + 1));

		scanner.close();

	}
}