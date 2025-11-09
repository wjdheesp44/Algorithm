import java.io.*;
import java.util.*;
public class Main {
    static int[] cube;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        cube = new int[25];
        for(int i = 1; i <= 24; i++){
            cube[i] = Integer.parseInt(st.nextToken());
        }
        
        System.out.println(moveCube());
    }

    private static int moveCube() {
        leftUp();
        if (check()) return 1;
        leftDown();
//        System.out.println(Arrays.toString(cube));

        leftDown();
        if (check()) return 1;
        leftUp();
//        System.out.println(Arrays.toString(cube));

        rightUp();
        if (check()) return 1;
        rightDown();
//        System.out.println(Arrays.toString(cube));

        rightDown();
        if (check()) return 1;
        rightUp();
//        System.out.println(Arrays.toString(cube));

        upLeft();
        if (check()) return 1;
        upRight();
//        System.out.println(Arrays.toString(cube));

        upRight();
        if (check()) return 1;
        upLeft();
//        System.out.println(Arrays.toString(cube));

        downLeft();
        if (check()) return 1;
        downRight();
//        System.out.println(Arrays.toString(cube));

        downRight();
        if (check()) return 1;
        downLeft();
//        System.out.println(Arrays.toString(cube));

        nextLeftUp();
        if (check()) return 1;
        nextLeftDown();

        nextLeftDown();
//        System.out.println(Arrays.toString(cube));
        if (check()) return 1;
        nextLeftUp();

//        System.out.println(Arrays.toString(cube));

        nextRightUp();
        if (check()) return 1;
        nextRightDown();

        nextRightDown();
        if (check()) return 1;
        nextRightUp();

        return 0;
    }

    private static void leftUp() {
        int c1 = cube[1];
        int c2 = cube[3];
        cube[1] = cube[5];
        cube[3] = cube[7];
        cube[5] = cube[9];
        cube[7] = cube[11];
        cube[9] = cube[24];
        cube[11] = cube[22];
        cube[24] = c1;
        cube[22] = c2;
        int c = cube[13];
        cube[13] = cube[14];
        cube[14] = cube[16];
        cube[16] = cube[15];
        cube[15] = c;
    }

    private static void leftDown() {
        int c1 = cube[5];
        int c2 = cube[7];
        cube[5] = cube[1];
        cube[7] = cube[3];
        cube[1] = cube[24];
        cube[3] = cube[22];
        cube[24] = cube[9];
        cube[22] = cube[11];
        cube[9] = c1;
        cube[11] = c2;
        int c = cube[13];
        cube[13] = cube[15];
        cube[15] = cube[16];
        cube[16] = cube[14];
        cube[14] = c;
    }

    private static void rightUp() {
        int c1 = cube[2];
        int c2 = cube[4];
        cube[2] = cube[6];
        cube[4] = cube[8];
        cube[6] = cube[10];
        cube[8] = cube[12];
        cube[10] = cube[23];
        cube[12] = cube[21];
        cube[23] = c1;
        cube[21] = c2;
        int c = cube[17];
        cube[17] = cube[19];
        cube[19] = cube[20];
        cube[20] = cube[18];
        cube[18] = c;
    }

    private static void rightDown() {
        int c1 = cube[6];
        int c2 = cube[8];
        cube[6] = cube[2];
        cube[8] = cube[4];
        cube[2] = cube[23];
        cube[4] = cube[21];
        cube[23] = cube[10];
        cube[21] = cube[12];
        cube[10] = c1;
        cube[12] = c2;
        int c = cube[17];
        cube[17] = cube[18];
        cube[18] = cube[20];
        cube[20] = cube[19];
        cube[19] = c;
    }

    private static void upLeft() {
        int c1 = cube[5];
        int c2 = cube[6];
        cube[5] = cube[17];
        cube[6] = cube[18];
        cube[17] = cube[21];
        cube[18] = cube[22];
        cube[21] = cube[13];
        cube[22] = cube[14];
        cube[13] = c1;
        cube[14] = c2;
        int c = cube[1];
        cube[1] = cube[3];
        cube[3] = cube[4];
        cube[4] = cube[2];
        cube[2] = c;
    }

    private static void upRight() {
        int c1 = cube[5];
        int c2 = cube[6];
        cube[5] = cube[13];
        cube[6] = cube[14];
        cube[13] = cube[21];
        cube[14] = cube[22];
        cube[21] = cube[17];
        cube[22] = cube[18];
        cube[17] = c1;
        cube[18] = c2;
        int c = cube[1];
        cube[1] = cube[2];
        cube[2] = cube[4];
        cube[4] = cube[3];
        cube[3] = c;
    }

    private static void downLeft() {
        int c1 = cube[7];
        int c2 = cube[8];
        cube[7] = cube[19];
        cube[8] = cube[20];
        cube[19] = cube[23];
        cube[20] = cube[24];
        cube[23] = cube[15];
        cube[24] = cube[16];
        cube[15] = c1;
        cube[16] = c2;
        int c = cube[9];
        cube[9] = cube[10];
        cube[10] = cube[12];
        cube[12] = cube[11];
        cube[11] = c;
    }

    private static void downRight() {
        int c1 = cube[7];
        int c2 = cube[8];
        cube[7] = cube[15];
        cube[8] = cube[16];
        cube[15] = cube[23];
        cube[16] = cube[24];
        cube[23] = cube[19];
        cube[24] = cube[20];
        cube[19] = c1;
        cube[20] = c2;
        int c = cube[9];
        cube[9] = cube[11];
        cube[11] = cube[12];
        cube[12] = cube[10];
        cube[10] = c;
    }

    private static void nextLeftUp() {
        int c1 = cube[3];
        int c2 = cube[4];
        cube[3] = cube[17];
        cube[4] = cube[19];
        cube[17] = cube[10];
        cube[19] = cube[9];
        cube[10] = cube[16];
        cube[9] = cube[14];
        cube[16] = c1;
        cube[14] = c2;
        int c = cube[5];
        cube[5] = cube[6];
        cube[6] = cube[8];
        cube[8] = cube[7];
        cube[7] = c;
    }

    private static void nextLeftDown() {
        int c1 = cube[3];
        int c2 = cube[4];
        cube[3] = cube[16];
        cube[4] = cube[14];
        cube[16] = cube[10];
        cube[14] = cube[9];
        cube[10] = cube[17];
        cube[9] = cube[19];
        cube[17] = c1;
        cube[19] = c2;
        int c = cube[5];
        cube[5] = cube[7];
        cube[7] = cube[8];
        cube[8] = cube[6];
        cube[6] = c;
    }

    private static void nextRightUp() {
        int c1 = cube[1];
        int c2 = cube[2];
        cube[1] = cube[18];
        cube[2] = cube[20];
        cube[18] = cube[12];
        cube[20] = cube[11];
        cube[12] = cube[15];
        cube[11] = cube[13];
        cube[15] = c1;
        cube[13] = c2;
        int c = cube[21];
        cube[21] = cube[23];
        cube[23] = cube[24];
        cube[24] = cube[22];
        cube[22] = c;
    }

    private static void nextRightDown() {
        int c1 = cube[1];
        int c2 = cube[2];
        cube[1] = cube[15];
        cube[2] = cube[13];
        cube[15] = cube[12];
        cube[13] = cube[11];
        cube[12] = cube[18];
        cube[11] = cube[20];
        cube[18] = c1;
        cube[20] = c2;
        int c = cube[21];
        cube[21] = cube[22];
        cube[22] = cube[24];
        cube[24] = cube[23];
        cube[23] = c;
    }

    private static boolean check() {
        for (int i = 1; i <= 21; i += 4) {
            if (cube[i] != cube[i+1] || cube[i+1] != cube[i+2]
            || cube[i+2] != cube[i+3]) {
                return false;
            }
        }
        return true;
    }
}