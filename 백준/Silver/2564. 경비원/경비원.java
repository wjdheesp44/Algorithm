import java.util.*;
import java.io.*;
public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int[] dir = {0, 2, 1, 4, 3}; // 북: 1, 남: 2, 동: 4, 서: 3 
		int result = 0;
		st = new StringTokenizer(br.readLine());
		int C = Integer.parseInt(st.nextToken());
		int R = Integer.parseInt(st.nextToken());
		
		int storeCnt = Integer.parseInt(br.readLine());
		int[][] stores = new int[storeCnt][2];
		for (int i = 0; i < storeCnt; i++) {
			st = new StringTokenizer(br.readLine());
			stores[i][0] = Integer.parseInt(st.nextToken());
			stores[i][1] = Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(br.readLine());
		int dongDir = Integer.parseInt(st.nextToken());
		int dongX = Integer.parseInt(st.nextToken());

		for (int i = 0; i < storeCnt; i++) {
			if (dongDir == stores[i][0]) {
				result += Math.abs(stores[i][1]-dongX);
			} else if (dongDir == dir[stores[i][0]]) { // 반대쪽
				int a = 0;
				int b = 0;
				if (dongDir == 1 || dongDir == 2) {
					a = R + stores[i][1] + dongX;
					b = R + 2*C - (stores[i][1] + dongX);
				} else {
					a = C + stores[i][1] + dongX;
					b = C + 2*R - (stores[i][1] + dongX);
				}
				result += Math.min(a, b);
			} else {
				if (dongDir + stores[i][0] == 4) {
					result += dongX + stores[i][1];
				} else if (dongDir + stores[i][0] == 5) {
					if (dongDir == 1) {
						result += C - dongX + stores[i][1];
					} else if (dongDir == 2) {
						result += dongX + R - stores[i][1];
					} else if (dongDir == 3) {
						result += R - dongX + stores[i][1];
					} else {
						result += dongX + C - stores[i][1];
					}
				} else {
					result += R + C - dongX - stores[i][1];
				}
			}
		}
		System.out.println(result);
	}
}