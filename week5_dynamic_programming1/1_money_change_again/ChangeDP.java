import java.util.Scanner;

public class ChangeDP {
    private static int getChange(int money) {
       int[] coins = {1, 3, 4};
        int[] MinNumCoins = new int[money+1];
        MinNumCoins[0] = 0;
        for (int m = 1; m <= money; m++){
            MinNumCoins[m] = Integer.MAX_VALUE;
            for (int i = 0; i < 3; i++){
                if (m >= coins[i]){
                    int NumCoins = MinNumCoins[m - coins[i]] + 1;
                    if (NumCoins < MinNumCoins[m]){
                        MinNumCoins[m] = NumCoins;
                    }
                }
            }
        }
        //write your code here
        return MinNumCoins[money];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int money = scanner.nextInt();
        System.out.println(getChange(money));

    }
}

