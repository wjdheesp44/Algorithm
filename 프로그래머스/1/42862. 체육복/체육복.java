import java.util.*;
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        int[] arr = new int[n+1];
        for (int l : lost) arr[l]--;
        for (int r : reserve) arr[r]++;
        
        for (int i = 1; i <= n; i++) {
            if (i-1 > 0 && arr[i] > 0 && arr[i-1] < 0) {
                arr[i-1]++; arr[i]--;
            }
            if (i+1 <= n && arr[i] > 0 && arr[i+1] < 0) {
                arr[i+1]++; arr[i]--;
            }
        }
        for (int i = 1; i <= n; i++) {
            if (arr[i] >= 0) answer++;
        }
        
        return answer;
    }
}