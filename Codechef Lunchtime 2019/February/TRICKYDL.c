#include <stdio.h>
#include <stdlib.h>

int main()
{
    long int c,a, sum, diff;
    long int t;
    int i,d1, d2, flag=0;
    scanf("%d", &t);
    while(t>0)
    {
        t--;
        scanf("%d", &a);
        sum=a-1;
        c=1;
        i=1;
        while(sum>0)
        {
            c=c*2;
            diff=a-c;
            if(diff<=0 && flag==0)
            {
                d2=i;
                flag=1;
            }
            sum=sum+diff;
            if(sum<=0)
                d1=i;
            i++;
        }
        printf("%d\t%d\n", d1, d2);
        flag=0;
    }
    return 0;
}
