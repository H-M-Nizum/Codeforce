#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    string c = "codeforces";
    while(t--){
        int ans = 0;
        string s;
        cin>>s;
        for(int i=0; i<10; i++){
            if(s[i] != c[i]) ans++;
        }
        cout<<ans<<endl;
    }

    return 0;
}