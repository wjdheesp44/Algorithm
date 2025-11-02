import java.io.*;
import java.util.*;
public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String arrOrigin = br.readLine();
		int N = arrOrigin.length();
		int[] arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = arrOrigin.charAt(i) - '0';
		}
		
		if (arr[0] == 0) {
			System.out.println(0);
			return;
		}
		if (N == 1) {
			System.out.println(1);
			return;
		}
		
		long[] dp = new long[N+1];
		dp[0] = 1;
		dp[1] = 1;
		if (arr[0]*10 + arr[1] > 26 && N == 2) {
			if (arr[1] == 0) System.out.println(0);
			else System.out.println(1);
			return;
		}
		
		for (int i = 1; i < N; i++) {
			int num = arr[i-1]*10 + arr[i];
			int total = 0;
			if (arr[i] > 0) {
				total += dp[i];
			}
			if (num <= 26 && num >= 1 && arr[i-1] > 0) {
				total += dp[i-1];
			}
			dp[i+1] = total%1000000;
		}
		System.out.println(dp[N]);
	}
}