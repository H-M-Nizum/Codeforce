#include<bits/stdc++.h>
using namespace std;
int main(){
    int n, q;
    cin>>n>>q;
    vector<int> v(n);
    for(int i=0; i<n; i++){
        cin>>v[i];
    }
    vector<long long> ans;
    long long s = 0;
    ans.push_back(s);
    for(long long i:v){
        s += i;
        ans.push_back(s);
    }
    while (q--)
    {
        int l, r;
        cin>>l>>r;
        cout<<ans[r] - ans[l-1]<<endl;
    }
    

    return 0;
}