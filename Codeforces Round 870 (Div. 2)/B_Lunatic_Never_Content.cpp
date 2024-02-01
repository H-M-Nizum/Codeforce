#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    
    while(t--){
        int n;
        cin>>n;
        int a[n];
        for(int i=0; i<n; i++){
            cin>>a[i];
        }

        vector<int> v;

        for(int i=0; i<n; i++){
            if(a[i] - a[n-i-1] > 0) v.push_back(a[i] - a[n-i-1]);
        }

        int ans = 0;
        for(int val:v){
            ans = __gcd(val, ans);
        }
        cout<<ans<<endl;
    }

    return 0;
}