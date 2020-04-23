#include <stdio.h>
#include <stdlib.h>
int sum_digits(long long int n)
{

}
int main()
{
    long long int t,n,d,count=0,minvalue;
    scanf("%lld",&t);
    while(t>0)
    {   long long int digit,sum=0;
        t=t-1;
        scanf("%lld %lld",&n,&d);
       while()
       if(n/10=0)
       {  n=n+d;
          count = count+1;
          temp=n;
          while(temp>0)
          {
              temp=temp%10;
              sum=sum+temp;
              temp=temp%10;
         }
         count=count+1;
         sum=sum+d;








/*int main()
{
int i,j,n,m,temp;
scanf("%d",&n);
int a[n];
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}

for(i=0;i<n-1;i++)
{  for(j=0;j<n-1-i;j++)
   {
       if(a[j]>a[j+1])
       {
           temp=a[j];
           a[j]=a[j+1];
           a[j+1]=temp;
       }
   }
   }
   for(int k=0;k<n;k++)
   {
       printf("%4d",a[k]);
   }
}
*/
