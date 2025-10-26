import java.io.*;
import java.util.*;
public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		int[] month = new int[13];
		month[1] = 31; month[2] = 28; month[3] = 31; month[4] = 30; month[5] = 31;
		month[6] = 30; month[7] = 31; month[8] = 31; month[9] = 30; month[10] = 31;
		month[11] = 30; month[12] = 31;
		int[][] flowers = new int[N][2];
		int[] first = new int[4];
		int[] end = new int[4];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());
			flowers[i][0] = a * 100 + b;
			flowers[i][1] = c * 100 + d;
		}
		
		//301, 1130
		Arrays.sort(flowers, (a, b) -> {
			if (a[0] != b[0]) {
				return Integer.compare(a[0], b[0]);
			}
			return Integer.compare(b[1], a[1]);
		});
		
		int cnt = 0;
		int curDay = 301;
		int maxEnd = 0;
		int idx = 0;
		while (curDay < 1201) {
//			System.out.println("?" + curDay);
			for (int i = idx; i < N; i++) {
//				System.out.println("i : " + i);
				if (flowers[i][0] <= curDay && flowers[i][1] > maxEnd) {
					idx = i;
					maxEnd = flowers[i][1];
				} else if (flowers[i][0] > curDay) break;
			}
			
			if (maxEnd == curDay) {
			    System.out.println(0);
			    return;
			}
			
			cnt++;
			curDay = maxEnd;
		}
		System.out.println(cnt);
	}

}
