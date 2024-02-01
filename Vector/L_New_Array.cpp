#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    vector<int> v1(n), v2(n), v;
    for(int i=0; i<n; i++){
        cin>>v1[i];
    }
    for(int i=0; i<n; i++){
        cin>>v2[i];
    }
    v = v1;
    v.insert(v.begin(), v2.begin(), v2.end());
    for(int i=0; i<v.size(); i++){
        cout<<v[i]<<" ";
    }
    cout<<endl;
    return 0;
}