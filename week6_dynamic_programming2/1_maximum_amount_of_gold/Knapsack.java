import java.util.*;


public class Knapsack {
    static int max(int a, int b)
    {
        return (a > b)? a : b;
    }

    static int optimalWeight(int n, int W, int[] wt) {
        int[][] K = new int[n+1][W+1];
        for (int i = 0; i <= n; i++){
            for (int w = 0; w <= W; w++){
                if (i == 0 || w == 0)
                    K[i][w] = 0;
                else if (wt[i-1] <= w)
                    K[i][w] = max(wt[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]);
                else
                    K[i][w] = K[i-1][w];
            }
        }
        return K[n][W];
        /*int[][] value = new int[W+1][n+1];
        for (int i = 0; i <= n; i++){
            value[0][i] = 0;
        }
        for (int ww = 0; ww <= W; ww++){
            value[ww][0] = 0;
        }
        for (int i = 1; i <= n; i++){
            for (int ww = 1; ww <= W; ww++){
                value[ww][i] = value[ww][i-1];
                if (w[i] <= ww){
                    int val = value[ww-1][i-1] + w[i];
                    if (value[ww][i] < val){
                        value[ww][i] = val;
                    }
                }
            }
        }
        return value[W][n];*/
        //write you code here
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int W, n;
        W = scanner.nextInt();
        n = scanner.nextInt();
        int[] wt = new int[n+1];
        for (int i = 0; i < n; i++) {
            wt[i] = scanner.nextInt();
        }
        //w[0] = 0;
        System.out.println(optimalWeight(n, W, wt));
    }
}




// public class Knapsack {
//     static int optimalWeight(int W, int[] w) {
//         //write you code here
//         int result = 0;
//         for (int i = 0; i < w.length; i++) {
//           if (result + w[i] <= W) {
//             result += w[i];
//           }
//         }
//         return result;
//     }

//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
//         int W, n;
//         W = scanner.nextInt();
//         n = scanner.nextInt();
//         int[] w = new int[n];
//         for (int i = 0; i < n; i++) {
//             w[i] = scanner.nextInt();
//         }
//         System.out.println(optimalWeight(W, w));
//     }
// }

