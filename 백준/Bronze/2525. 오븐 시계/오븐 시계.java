import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		int A = scanner.nextInt();
		int B = scanner.nextInt();
		int C = scanner.nextInt();

		if ((B + C) < 60) {
			System.out.println(A + " " + (B + C));
		} else {
			int D = (B + C) / 60;
			int F = (B + C) % 60;
			if ((A + D) < 24) {
				System.out.println((A + D) + " " + F);
			} else {
				System.out.println((A + D - 24) + " " + F);
			}
		}

	}
}
