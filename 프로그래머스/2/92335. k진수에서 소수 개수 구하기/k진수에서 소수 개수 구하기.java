import java.util.*;

class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        String num = Integer.toString(n, k);
        String[] arr = num.split("0");
        
        out : for (String a : arr) {
            if (a.isEmpty()) continue;
            long tmp = Long.parseLong(a);
            if (tmp == 1) continue;
            for (int i = 2; i <= Math.sqrt(tmp); i++) {
                if (tmp % i == 0) {
                    continue out;
                }
            }
            answer++;
            System.out.println(a);
        }
        
        return answer;
    }
}