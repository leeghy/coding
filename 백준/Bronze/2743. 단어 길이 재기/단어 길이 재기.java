import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		String word = scanner.next();

		char[] arr = word.toCharArray();

		int num = 0;
		for (char c : arr) {
			num++;
		}

		System.out.println(num);
		scanner.close();

	}

}