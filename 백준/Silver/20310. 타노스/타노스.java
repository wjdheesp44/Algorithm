import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String S = br.readLine();
		int N = S.length();
		int zero = 0;
		int one = 0;
		boolean[] remove = new boolean[N];
		
		for (int i = 0; i < N; i++) {
			if (S.charAt(i) == '0') {
				zero++;
			} else {
				one++;
			}
		}

		zero /= 2;
		one /= 2;
		for (int j = 0; j < N; j++) {
			if (S.charAt(j) == '1' && one > 0) {
				one--;
				remove[j] = true;
			}
		}

		for (int j = N-1; j >= 0; j--) {
			if (S.charAt(j) == '0' && zero > 0) {
				  zero--;
				  remove[j] = true;
			}
		}

		String result = "";
		for (int i = 0; i < N; i++) {
			if (remove[i]) continue;
			result += S.charAt(i);
		}
		System.out.println(result);
	}
}