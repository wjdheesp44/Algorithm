import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		int[] arrN = new int[N];

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			arrN[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(arrN);
		
		int M = Integer.parseInt(br.readLine());
		int[] arrM = new int[M];

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < M; i++) {
			arrM[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int num : arrM) {
			int isExist = 0;
			int lt = 0;
			int rt = N-1;
			while (lt <= rt) {
				int mid = (lt + rt) / 2;
				
				if (arrN[mid] == num) {
					isExist = 1;
					break;
				} else if (arrN[mid] > num) {
					rt = mid - 1;
				} else {
					lt = mid + 1;
				}
			}
			sb.append(isExist).append(" ");
		}
		System.out.println(sb);
	}
}