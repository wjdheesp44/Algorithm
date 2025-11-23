import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] arr = new int[4];
		int ans = 0;
		String str = "";
		for (int i = 0; i < 4; i++) {
			str += st.nextToken();
		}
		ans = Integer.parseInt(str);
		arr[0] = ans;
		
		for (int i = 1; i < 4; i++) {
			int first = ans / 1000;
			int last = ans % 1000;
			ans = last * 10 + first;
			arr[i] = ans;
		}
		Arrays.sort(arr);
//		System.out.println(Arrays.toString(arr));
		ans = arr[0];
//		System.out.println("답: " + ans);
		HashSet<Integer> set = new HashSet<>();
		
		for (int i = 1; i <= 9; i++) {
			for (int j = 1; j <= 9; j++) {
				for (int k = 1; k <= 9; k++) {
					for (int l = 1; l <= 9; l++) {
						int[] num = new int[4];
						num[0] = i*1000 + j*100 + k*10 + l;
						int num2 = num[0];
						for (int a = 1; a < 4; a++) {
							int first = num2 / 1000;
							int last = num2 % 1000;
							num2 = last * 10 + first;
							num[a] = num2;
						}
						Arrays.sort(num);
//						System.out.println(num[0]);
						set.add(num[0]);
					}
				}
			}
		}
		
		ArrayList<Integer> list = new ArrayList<>(set);
		list.sort(null);
		
		for (int i = 0; i < list.size(); i++) {
//			System.out.println(list.get(i));
			if (ans == list.get(i)) {
				System.out.println(i+1);
				return;
			}
		}
	}
}
