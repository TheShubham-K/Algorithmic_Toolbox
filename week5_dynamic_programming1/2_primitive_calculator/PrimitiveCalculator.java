
import java.util.*;

public class PrimitiveCalculator {
    private static int optimal_sequence(int n) {
        int[] MinNum = new int[n + 1];
        MinNum[1] = 0;
        for (int m = 2; m <= n; m++){
            MinNum[m] = Integer.MAX_VALUE;
            if (m % 3 == 0){
                int Num = MinNum[m / 3] + 1;
                if (Num < MinNum[m]){
                    MinNum[m] = Num;
                }
            } else if (m % 2 == 0){
                int Num = MinNum[m / 2] + 1;
                if (Num < MinNum[m]){
                    MinNum[m] = Num;
                }
            }
            int Num = MinNum[m - 1] + 1;
            if (Num < MinNum[m]){
                MinNum[m] = Num;
                }
        }
        return MinNum[n];

        /*List<Integer> sequence = new ArrayList<Integer>();
        while (n >= 1) {
            sequence.add(n);
            if (n % 3 == 0) {
                n /= 3;
            } else if (n % 2 == 0) {
                n /= 2;
            } else {
                n -= 1;
            }
        }
        Collections.reverse(sequence);
        return sequence;*/
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        /*List<Integer> sequence = optimal_sequence(n);
        System.out.println(sequence.size() - 1);
        for (Integer x : sequence) {
            System.out.print(x + " ");
        }*/
        System.out.println(optimal_sequence(n));
    }
}

