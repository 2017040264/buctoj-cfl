#include<iostream>
#include<cstring>
using namespace std;


int main(){
 int n;
 cin>>n;
bool a[100000000];

  for(int i=2;i<=n;i++)
  {
     if (!a[i]){
         cout<<i<<endl;
         if ((long long)i*i >n)
          continue;
         for (int j=i*i;j<=n;j+=i){
             a[j]=true;
         }
     }
  }

}
    