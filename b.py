#include <bits/stdc++.h>
#include <math.h>
#include <algorithm>
#include <string.h>
#include <climits>
using namespace std;
#define mod 998244353
int precd(char d) 
{
    if(d == '|' || d == '^' || d == '&') 
    return 1; 
    else
    return -1; 
}
string infixPostfix(string s) 
{ 
    std::stack<char> st1; 
    st1.push('M'); 
    int l = s.length(); 
    string news; 
    for(int i = 0; i < l; i++) 
    {
        if(s[i] == '#') 
        news+=s[i];
        else if(s[i] == '(') 
        st1.push('(');
        else if(s[i] == ')') 
        { 
            while(st1.top() != 'M' && st1.top() != '(') 
            { 
                char d = st1.top(); 
                st1.pop(); 
               news += d; 
            } 
            if(st1.top() == '(') 
            { 
                char d = st1.top(); 
                st1.pop(); 
            } 
        }
        else{ 
            while(st1.top() != 'M' && precd(s[i]) <= precd(st1.top())) 
            { 
                char d = st1.top(); 
                st1.pop(); 
                news += d; 
            } 
            st1.push(s[i]); 
        } 
    }
    while(st1.top() != 'M') 
    { 
        char d = st1.top(); 
        st1.pop(); 
        news += d; 
    }
    return news;
}

vector<long long> aandfunc(vector<long long> a1,vector<long long> b1)
{
    vector<vector<int>>temp1{{0,0,0,0},
                            {0,1,2,3},
                            {0,2,2,0},
                            {0,3,0,3}};
    vector<long long>ans1{0,0,0,0};
    for(int i = 0;i<temp1.size();i++)
    {
        for(int j = 0;j<temp1[0].size();j++)
        {
            ans1[temp1[i][j]] = ans1[temp1[i][j]] + (a1[i] * b1[j]);
        }
    }
    return ans1;
}

vector<long long> xoorfunc(vector<long long> a1,vector<long long> b1)
{
    vector<vector<int>>tem{{0,1,2,3},
                            {1,0,3,2},
                            {2,3,0,1},
                            {3,2,1,0}};
    vector<long long>an{0,0,0,0};
    for(int i = 0;i<tem.size();i++)
    {
        for(int j = 0;j<tem[0].size();j++)
        {
            an[tem[i][j]] = an[tem[i][j]] + (a1[i] * b1[j]);
        }
    }
    return an;
}

vector<long long> orrfunc(vector<long long> a1,vector<long long> b1)
{
    vector<vector<int>>tem{{0,1,2,3},
                            {1,1,1,1},
                            {2,1,2,1},
                            {3,1,1,3}};
    vector<long long>an{0,0,0,0};
    for(int i = 0;i<tem.size();i++)
    {
        for(int j = 0;j<tem[0].size();j++)
        {
            an[tem[i][j]] = an[tem[i][j]] + (a1[i] * b1[j]);
        }
    }
    return an;
}

vector<long long> evaluatePost(string exp)  
{
    stack<vector<long long>> st1;  
    for (long i = 0; exp[i]; ++i)  
    { 
        if (exp[i] == '#') 
        {
            vector<long long>temp{1,1,1,1};
            st1.push(tmp);
        }
        else
        {
            vector<long long> vaal1,vaal2;
            vaal1 = st1.top();st1.pop();
            vaal2 = st1.top();st1.pop();
            switch (exp[i])  
            {  
            case '&': st1.push(aandfunc(vaal1,vaal2)); break;  
            case '^': st1.push(xoorfunc(vaal1,vaal2)); break;  
            case '|': st1.push(orrfunc(vaal1,vaal2)); break;
            }  
        }  
    }
    return st1.top();
}

long long tops(string s)
{
    long long count1 = 0;
    for(long i = 0;i < s.length();i++)
    {
        if(s[i] == '#'){++count1;}
    }
    return count1;
}

long long int powerup(long long int x1, unsigned long long int y1, unsigned long long int m1)
{
    if (y1 == 0)
        return 1;
    long long int p1 = powerup(x1, y1/2, m1) % m1;
    p1 = (p1* p1) % m1;
 
    return (y1%2 == 0)? p1 : (x1 * p1) % m1;
}
 
long long int gcdd(long long int a1, long long int b1)
{
    if (a1 == 0)
        return b1;
    return gcdd(b1%a1, a1);
}
long long int modi(long long int a1, long long int m1)
{
    long long int g1 = gcdd(a1, m1);
 
            return powerup(a1, m1-2, m1);

}
void solution(string s) 
{
    s = infixToPostfix(s);
   // cout<<s;
    long long count = getops(s);
    count = (long long)(pow(4,count)+0.5);
    // cout << count << endl;
    evaluatePostfix(s);
    vector<long long> v = evaluatePostfix(s);
    for(int i = 0;i < 4;i++)
    {
        long long p=v[i];
        long long temp=count;
   //cout<<p<<" "<<temp<<"\n";
        long long q = modInverse(temp, mod);
        v[i] = ((p % mod) * (q % mod)) % mod;
    }
    cout << v[0] << " " << v[1] << " " << v[2] << " " << v[3] << endl;

}

//driver
int main() {
    // ios_base::sync_with_stdio(false);
    // cin.tie(NULL);
    // #ifndef ONLINE_JUDGE
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    // #endif
    long test;cin>>test;
    while(test--)
    {
        string s;cin>>s;
        solve(s);
    }
}
