#include<iostream>
using namespace std;
int main()
{
    
    
    for(int i=0;i<10;i++)
    {
        cout<<'\n'<<i<<': ';
        for(int j=0;j<i;j++)
        {
            cout<<j;
        }
    }
    
    return 0;
}