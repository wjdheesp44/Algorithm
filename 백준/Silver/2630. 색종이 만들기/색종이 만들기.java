import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int N, bad, good;
	static int[][] spaces;
	
	public static void main(String[] args) throws Exception{
		N = Integer.parseInt(br.readLine());
		
		spaces = new int[N][N];
		for (int i = 0 ; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				spaces[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		makeTile(0, 0, N);
		sb.append(good).append("\n");
		sb.append(bad).append("\n");
		System.out.println(sb);
	}
	
	private static void makeTile(int x, int y, int size) {
		int sum = 0;
		for (int i = x; i < x+size; i++) {
			for (int j = y; j < y+size; j++) {
				sum += spaces[i][j];
			}
		}
		
		int newSize = size/2;
		if (sum == size*size) {
			bad++;
		} else if (sum == 0) {
			good++;
		} else {
			makeTile(x, y, newSize);
			makeTile(x+newSize, y, newSize);
			makeTile(x, y+newSize, newSize);
			makeTile(x+newSize, y+newSize, newSize);
		}	
	}
}