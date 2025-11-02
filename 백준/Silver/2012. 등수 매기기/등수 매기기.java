import java.io.*;
import java.util.*;
public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		long[] arr = new long[N];
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}

		Arrays.sort(arr);
		
		long result = 0;
		for (int i = 0; i < N; i++) {
			result += Math.abs(arr[i] - (i+1));
		}
		System.out.println(result);
	}
}