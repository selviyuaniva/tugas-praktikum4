#include<iostream>
using namespace std;

int main ()
{
	cout << "(";
	for (int a=1;a<=25;a++)
	{
		if (a%5!=0)
		{
		cout << a << ",";	
		}
	}
		cout << ")";
	return 0;
	
}
