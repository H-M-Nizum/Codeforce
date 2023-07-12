#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int f = 1000000;
        int l = 1000000;
        int ans = 1000000;
        for(int i=0; i<n; i++){
            int m;
            string s;
            cin>>m>>s;
            if(s[0] == '1'){
                f = min(f, m);
            }
            if(s[1] == '1'){
                l = min(l, m);
            }
            if(s[0] == '1' && s[1] == '1'){
                ans = min(ans, m);
            }
   
            
        }

        long long result = min(ans, f+l);
        if(result >= 1000000){
            cout<<-1<<endl;
        }
        else{
            cout<<result<<endl;
        }
        
    }

    return 0;
}