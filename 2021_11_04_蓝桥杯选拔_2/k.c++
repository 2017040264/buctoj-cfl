#include<iostream>
#include<cstring>
using namespace std;


int main(){
 int m,k,x;
 cin>>m>>k;

 int arr[k];
 for(int i=0;i<k;i++){
     arr[i]=1000000;
 }

 for(int i=0 ;i<m;i++){

     cin>>x;
     
    for(int j=0;j<k;j++){
       if(arr[j]>x){
         for(int e=k-1;e>j;e--){
             arr[e]=arr[e-1];
         }
         arr[j]=x;
       }
         }
     } 

cout<<arr[k]<<endl;
     
 }


