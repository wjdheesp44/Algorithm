import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        // System.out.println(commands.length);
        // int[] answer = {};
        int[] answer = new int[commands.length];
        int i = 0;
        for (int[] command : commands) {
            int arrSize = command[1] - command[0] + 1;
            // System.out.println(arrSize);
            int[] arr = new int[arrSize];
            System.arraycopy(array, command[0]-1, arr, 0, arrSize);
            Arrays.sort(arr);
            answer[i++] = arr[command[2]-1];
        }
        return answer;
    }
}