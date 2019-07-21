#include <stdio.h>

int main()
{
int e,n;
long pow=1;
scanf("%d %d",&n,&e);
while(e!=0)
    {
     pow=pow*n;
     --e;
     }
printf("%ld",pow);
}
