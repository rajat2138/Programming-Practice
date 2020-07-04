#include <stdio.h>
int main()
{
    int t, n, k, i;
    long int v, temp, sum;
    scanf("%d", &t);
    while(t>0)
    {
        t--;
        scanf("%d%d%ld", &n, &k, &v);
        sum=0;
        for(i=0;i<n;i++)
        {
            scanf("%ld", &temp);
            sum=sum+temp;
        }
        temp= ((n+k)*v) - sum;
        if(temp>0 && temp%k==0)
        {
            temp=temp/k;
            printf("%ld\n", temp);
        }
        else
            printf("-1\n");
    }
    return 0;
}
