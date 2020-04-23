#include <iostream>

using namespace std;

template <typename T>
T mymax( T x, T  y)
{
    return ((x>y)?x:y);
}

int main()
{
    cout<<mytax<int>(3,7)<<endl;
    cout<<mttax<char>('g','d')<<endl;
    return 0;
}
