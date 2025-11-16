import java.util.*;
import java.io.*;
public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int[] arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(arr);
		int[] result = new int[3];
		long ans = 3000000000L;
		out : for (int i = 0; i < N-2; i++) {
			for (int j = i+1; j < N-1; j++) {
				if (i == j) continue;
				int lt = j+1;
				int rt = N-1;
				while(lt <= rt) {
					int mid = (lt + rt) / 2;
					long total = (long) arr[i] + arr[j] + arr[mid];
					long totalAbs = Math.abs(total);
					if (totalAbs == 0) {
						result[0] = arr[i]; result[1] = arr[j]; result[2] = arr[mid];
						ans = 0;
						break out;
					} else if (totalAbs < ans) {
						if (total < 0) {
							lt = mid+1;
						} else {
							rt = mid-1;
						}
						result[0] = arr[i]; result[1] = arr[j]; result[2] = arr[mid];
						ans = totalAbs;
					} else {
						if (total < 0) {
							lt = mid+1;
						} else {
							rt = mid-1;
						}
					}
				}
			}
			
		}
		System.out.println(result[0] + " " + result[1] + " " + result[2]);
	}
}