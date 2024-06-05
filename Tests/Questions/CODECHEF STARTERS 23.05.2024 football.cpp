#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
    int t;
    cin>>t;
    for(int k=0;k<t;k++)
    {
        int i,j;
        cin>>i>>j;
        if(i==1 && j==1){
            cout<<"1";
        }
        else if(i==0 || j==0){
            cout<<"0";
        }
        else{
            while(i>=3){
                i=i-3;
            }
            while(j>=3){
                j=j-3;
            }
            if(i>j){
                cout<<i;
            }
            else{
                cout<<j;
            }
        }
        cout<<endl;
    }
}
