import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		String word = scanner.next();
		int n = scanner.nextInt();

		char c = word.charAt(n - 1);
		System.out.println(c);

		scanner.close();

	}

}