import java.io.*;
import java.util.*;


public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		int M = Integer.parseInt(st.nextToken());
		
		boolean[][] small = new boolean[N+1][N+1];
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			small[a][b] = true;
		}
		
		for (int k = 1; k <= N; k++) {
			for (int i = 1; i <= N; i++) {
				for (int j = 1; j <= N; j++) {
					if (small[i][k] && small[k][j]) small[i][j] = true;
				}
			}
		}
		
		int[] cnt = new int[N+1];
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (small[i][j] || small[j][i]) {
					cnt[i]++;
				}
			}
		}
		
		for (int i = 1; i <= N; i++) {
			sb.append(N-1-cnt[i]).append("\n");
		}
		System.out.println(sb);
	}
}