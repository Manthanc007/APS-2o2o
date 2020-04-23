#include <stdio.h>
#include <stdlib.h>
#include<math.h>
main()
{
    long long int t,a,n;
    long long int p=1,q=0,r=0;
    scanf("%lld",&t);
    while(t>0)
    {
      t=t-1;
      scanf("%lld",&n);
      if(n<=26)
      {
          if(n>2&&n<=10)
            {
            p=0;
            q=1;
            r=0;
            }
          else if(n>10&&n<=26)
          {
              { p=0;
                q=0;
                r=1;
              }
          }
      }
      else
      {
          a=(n-1)/26;
          p=pow(2,a);
          while(n>26)
          {
              n=n-26;
        }
           if(n>2&&n<=10)
            {

            q=p;
            p=0;
            r=0;
            }

          else if(n>10&&n<=26)
          {
                r=p;
                p=0;
                q=0;

                }
          else
            {
            p=pow(2,a);
            q=0;
            r=0;
}
      }

    printf("%lld %lld %lld\n",p,q,r);
}
}

