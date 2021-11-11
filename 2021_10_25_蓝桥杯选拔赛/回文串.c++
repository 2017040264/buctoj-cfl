#include<iostream>
#include<string.h>
using namespace std;

int main()
{
    int n;
    string ss;
    cin>>n;

    for(int i=0;i<n;i++)
    {
      cin>>ss;
    //   cout<<ss<<endl;
    //   cout<<ss.length()<<endl;
    //   cout<<ss[1]<<endl;
    int left=0;
    int rigth=ss.length()-1;
    int count=0;
    while(left<=rigth){
       if (ss[left]!=ss[rigth]) 
            count+=1;
       else if (count==0 && left==rigth)
            count+=1;
        
        left++;
        rigth--;
    }
        

    if (count==1)
        cout<<"YES"<<endl;
    else
        cout<<"NO"<<endl;
    }
}