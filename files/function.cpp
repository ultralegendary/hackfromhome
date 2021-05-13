#include<iostream>
using namespace std;
void function1()
{
cout<<"Hello function one \n";

}
void function2(int a)
{
    cout<<"Hello function two\n";
}
int main()
{
    function1();    // function call
    function2(10);  //sending an value

    return 0;
}