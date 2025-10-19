import java.io.*;
import java.util.*;

public class Main {
	static int N, K;
	static int[] belt, robots;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		belt = new int[2*N];
		robots = new int[2*N];
		
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < 2*N; i++) {
			belt[i] = Integer.parseInt(st.nextToken());
		}
		
		int brokenCnt = 0;
		int stage = 0;
		int[] tmp = new int[2*N];
		
		while (brokenCnt < K) {
			// [1] 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
			System.arraycopy(belt, 2*N-1, tmp, 0, 1);
			System.arraycopy(belt, 0, belt, 1, 2*N-1);
			System.arraycopy(tmp, 0, belt, 0, 1);
			
			System.arraycopy(robots, 2*N-1, tmp, 0, 1);
			System.arraycopy(robots, 0, robots, 1, 2*N-1);
			System.arraycopy(tmp, 0, robots, 0, 1);
			
			if (robots[N-1] == 1) {
				robots[N-1] = 0;
			}
			for (int j = N-2; j >= 0; j--) {
				if (robots[j+1] == 0 && robots[j] == 1 && belt[j+1] > 0) {
					robots[j] = 0; robots[j+1] = 1;
					belt[j+1]--;
				}
			}
			if (robots[N-1] == 1) {
				robots[N-1] = 0;
			}
			
			if (belt[0] > 0) {
				robots[0] = 1;
				belt[0]--;
			}
			
			brokenCnt = 0;
			for (int i = 0; i < 2*N; i++) {
				if (belt[i] == 0) {
					brokenCnt++;
				}
			}
			stage++;
		}
		System.out.println(stage);
	}
}
