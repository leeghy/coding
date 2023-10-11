import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		int T = scanner.nextInt();

		for (int i = 0; i < T; i++) {
			for (int j=0; j<T-i-1;j++) {
				System.out.print(" ");
			}
			for (int k=0;k<i+1;k++) {
				System.out.print("*");
			}
			System.out.println();
		}

	}
}