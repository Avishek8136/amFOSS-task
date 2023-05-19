#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    int m;
    int bill=0;
    scanf("%d",&n);
    scanf("%d",&m);
    if(n<m)
        bill=-1;
    else if(n==m)
        bill=n;
    else if(n>m)
    {
        bill=ceil(ceil(n/m)/2)*m;
        if((bill%m==0)&&(bill*2<n))
        {
            int f=n%(bill*2);
            bill=bill+f;
        }
        if(bill%m!=0)
        {
            int c=m-bill%m;
            bill=bill+c;
        }
    }
    printf("%d",bill);
    return 0;
}
