import java.io.*;
import java.util.*;
public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	public static void main(String[] args) throws Exception {
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int[] dp = new int[N+1];
		dp[0] = 0;
		for (int i = 1; i < N+1; i++) {
			dp[i] = N;
		}
		
		for (int i = 1; i <= N; i++) {
			for (int j = i-1; j >= 0; j--) {
				int leftmost_val = arr[j];
                
                int bunch_length = (i - 1) - j + 1;
                
                if (bunch_length <= leftmost_val) {
                    dp[i] = Math.min(dp[i], dp[j] + 1);
                }
			}
		}
		
		System.out.println(dp[N]);
	}
}