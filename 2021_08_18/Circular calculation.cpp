#include<iostream>
#include <iomanip>
using namespace std;
#define pi 3.14
int main(){
	
	float a,b;
	cin>>a>>b;
	cout<<setiosflags(ios::fixed);
    cout.precision(2); 
    float c1,sa,sb,va,vb;
    
    c1=2*pi*a;
    sa=a*pi*a;
    sb=4*a*pi*a;
    va=4*a*a*pi*a/3;
    vb=pi*a*a*b;
    
	cout<<"C1="<<c1<<endl;
	cout<<"Sa="<<sa<<endl;
	cout<<"Sb="<<sb<<endl;
	cout<<"Va="<<va<<endl;
	cout<<"Vb="<<vb<<endl;
	
	cout<<"\n%%%%%%%%%%%%%\n"<<endl;
	
	cout<<"C1="<<2*pi*a<<endl;
	cout<<"Sa="<<a*pi*a<<endl;
	cout<<"Sb="<<4*a*pi*a<<endl;
	cout<<"Va="<<4*a*a*pi*a/3<<endl;
	cout<<"Vb="<<pi*a*a*b<<endl;
	
	
	
}
