#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    vector<int> v(n);
    for(int i=0; i<n; i++){
        cin>>v[i];
    }
    sort(v.begin(), v.end());
    int count = 0, ans = 0;
    int value = v[0];
    for(int i=0; i<n; i++){
        if(value == v[i]) count++;
        else{
            if(value+1 == v[i]){
                ans += count;
            }
            count = 1;
            value=v[i];
        }
    }
    cout<<ans<<endl;
 
    return 0;
}