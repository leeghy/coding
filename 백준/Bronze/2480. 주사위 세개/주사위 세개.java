import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		int a = scanner.nextInt();
		int b = scanner.nextInt();
		int c = scanner.nextInt();
		
		if (a == b && b==c) {
			System.out.println(10000 + a*1000);
		}
		else if (a == b && b != c) {
			System.out.println(1000 + a*100);
		}
		else if (a == c && b != c) {
			System.out.println(1000 + a*100);
		}
		else if (c == b && a != c) {
			System.out.println(1000 + b*100);
		}
		else {
			if (a > b && a > c) {
				System.out.println(a*100); return;
			}
			if (b > c && b > a) {
				System.out.println(b*100); return;
			}
			if (c > b && c > a) {
				System.out.println(c*100); return;
			}
			
		}
	}
}
