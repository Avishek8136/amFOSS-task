import java.util.Scanner;

public class watertankblues {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();
        while(t>0){
            int count=0;
            int n = s.nextInt();
            int watercap[] = new int[n];
            for( int i = 0; i < n; i++) {
                watercap[i] = s.nextInt();
            }
            for (int i = 1; i < n; i++) {
                if(watercap[i]==0 && watercap[i-1]!=0)     {
                    watercap[i] = watercap[i]+1;
                    watercap[i-1] = watercap[i-1]-1;
                    count++;
                }
            }
            for(int i=0;i<n-1;i++){
                count=count+watercap[i];
            };
            System.out.println(count);
            t--;
        }
  
    }
}