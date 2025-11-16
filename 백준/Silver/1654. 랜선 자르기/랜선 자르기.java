import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int K = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		
		int[] wires = new int[K];
		int max = 0;
		for (int i = 0; i < K; i++) {
			wires[i] = Integer.parseInt(br.readLine());
			if (wires[i] > max) max = wires[i];
		}
		
		long lt = 1;
		long rt = max;
		long result = 0;
		while(lt <= rt) {
			long mid = (lt + rt) / 2;
			long cnt = 0;
			for (int w : wires) {
				cnt += w / mid;
			}

			if (cnt < N) {
				rt = mid - 1;
			} else {
				lt = mid + 1;
				result = Math.max(mid, result);
			}
		}
		System.out.println(result);
	}
}