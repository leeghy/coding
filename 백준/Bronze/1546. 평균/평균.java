import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		int N = scanner.nextInt();

		double sub[] = new double[N];

		double max = 0;

		for (int i = 0; i < N; i++) {
			sub[i] = scanner.nextInt();

			if (sub[i] > max) {
				max = sub[i];
			}
		}

		for (int i = 0; i < N; i++) {
			double tmp = sub[i];
			sub[i] = tmp / max * 100;
		}

		double sum = 0;
		for (int i = 0; i < N; i++) {
			sum += sub[i];
		}

		System.out.println(sum / N);

		scanner.close();

	}

}