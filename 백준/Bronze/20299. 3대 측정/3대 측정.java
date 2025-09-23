import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(st.nextToken());
		int S = Integer.parseInt(st.nextToken());
		int M= Integer.parseInt(st.nextToken());
		
		int[][] arr = new int[N][3];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			arr[i][0] = Integer.parseInt(st.nextToken());
			arr[i][1] = Integer.parseInt(st.nextToken());
			arr[i][2] = Integer.parseInt(st.nextToken());
		}
		
		ArrayList<Integer> result = new ArrayList<>();
		
		int cnt = 0;
		for (int i = 0; i < N; i++) {
			int sum = arr[i][0] + arr[i][1] + arr[i][2];
			if (sum < S) continue;
			boolean flag = true;
			for (int j = 0; j < 3; j++) {
				if (arr[i][j] < M) {
					flag = false;
				}
			}
			if (flag) {
				cnt++;
				sb.append(arr[i][0]).append(" ");
				sb.append(arr[i][1]).append(" ");
				sb.append(arr[i][2]).append(" ");
			}
		}
		System.out.println(cnt);
		System.out.println(sb);
		
	}
}