import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		int arr[] = new int[30];
		for (int i = 0; i < 30; i++) {
			arr[i] = i + 1;
		}

		for (int i = 0; i < 28; i++) {
			int num = scanner.nextInt();
			arr[num - 1] = 0;
		}
		
		for (int i=0;i<30;i++) {
			if (arr[i] != 0) {
				System.out.println(arr[i]);
			}
		}

		scanner.close();

	}
}