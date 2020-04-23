#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t>0)
	{
	    t--;
	    
	    int n,m;
	    cin>>n;
	    cin>>m;
	    
	    int count=0;
	    int flag=0;
	    
	    int x[n],y[m];
	    
	    for(int i=0;i<n;i++)
	    {
	        cin>>x[i];
	    }
	    
	    for(int i=0;i<m;i++)
	    {
	        cin>>y[i];
	    }
	    
	    sort(x,x+n);
	    sort(y,y+m);
	    
	    for(int i=0;i<n-1;i++)
	    {
	        if(x[i]==0)
	        {
	            count+=(n-1)*m;
	            flag=1;
	        }
	        else
	        {
	        for(int j=i+1;j<n;j++)
	        {
	            double dist=x[j]-x[i];
	            double a=sqrt(((pow(dist,2))-(pow(x[i],2)+pow(x[j],2)))/2);
	            if(a-int(a)==0)
	            {
	                for(int k=0;k<m;k++)
	                {
	                    if(abs(y[k])==a)
	                    {
	                        count++;
	                        //break;
	                        //cout<<"a is "<<a<<" x1 is "<<x[i]<<" x2 is "<<x[j]<<" y is "<<y[k]<<" count is "<<count<<endl;
	                    }
	                        
	                }
	            }
	        }
	        }
	    }
	    
	    
	    for(int i=0;i<m-1;i++)
	    {
	        if(flag!=1 && y[i]==0)
	        {
	            count+=n*(m-1);
	        }
	        else
	        {
	        for(int j=i+1;j<m;j++)
	        {
	            double dist=y[j]-y[i];
	            double a=sqrt(((pow(dist,2))-(pow(y[i],2)+pow(y[j],2)))/2);
	            if(a-int(a)==0)
	            {
	                for(int k=0;k<n;k++)
	                {
	                    if(abs(x[k])==a)
	                    {
	                        count++;
	                        //break;
	                        //cout<<"a is "<<a<<" y1 is "<<y[i]<<" y2 is "<<y[j]<<" x is "<<x[k]<<" count is "<<count<<endl;
	                    }
	                        
	                }
	            }
	        }
	        }
	    }
	    
	    cout<<count<<endl;
	    
	    
	    
	    
	}
	
	
	
	
	return 0;
}
