import java.io.*;
import java.util.*;

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
		
		int sum = arr[0];
		int[] A = new int[N];
		A[0] = arr[0];
		for (int i = 1; i < N; i++) {
			A[i] = A[i-1] + arr[i];
			sum += A[i];
		}
		
		System.out.println(sum);
	}
}