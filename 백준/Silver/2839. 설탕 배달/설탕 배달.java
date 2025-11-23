import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int result = 0;
		while(N >= 3) {
			if (N % 5 == 0) {
				result++;
				N -= 5;
			} else {
				result++;
				N -= 3;
			}
		}
		if (N != 0) {
			result = -1;
		}
		System.out.println(result);
	}
}