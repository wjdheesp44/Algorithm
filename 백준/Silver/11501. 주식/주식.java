import java.io.*;
import java.util.*;
public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int tc = 0; tc < T; tc++) {
			int N = Integer.parseInt(br.readLine());
			int[] arr = new int[N];
			
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}
			
			long result = 0;
			int max = 0;
			for (int i = N-1; i >= 0; i--) {
				if (arr[i] > max) { // 주식 올라갈 때
					max = arr[i];
				} else {
					result += (max - arr[i]);
				}
			}
			System.out.println(result);
		}
	}
}