import java.util.*;
import java.io.*;
public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		int[][] arr = new int[N][2];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int tmp = Integer.parseInt(st.nextToken());
			arr[i][0] = Integer.parseInt(st.nextToken());
			arr[i][1] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(arr, (a, b) -> {
			if (a[0] != b[0]) {
				return Integer.compare(a[0], b[0]);
			}
			return Integer.compare(a[1], b[1]);
		});
		
		PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> Integer.compare(a, b));
		for (int i = 0; i < N; i++) {
			if (!pq.isEmpty() && arr[i][0] >= pq.peek()) {
				pq.poll();
			}
			pq.offer(arr[i][1]);
		}
		System.out.println(pq.size());
	}
}