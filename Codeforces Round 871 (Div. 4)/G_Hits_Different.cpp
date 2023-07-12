#include<bits/stdc++.h>
using namespace std;

long long getsum(long long l, long long r){
    l--;
    long long ret = r*(r+1)*(2*r+1)/6 - l*(l+1)*(2*l+1)/6;
    return ret;
}
int main(){

    vector<int> v[10000];
    //make a pyramid use to vector.
    int a = 1;
    for(int i=1; i<10000; i++){
        for(int j=0; j<i; j++){
            v[i].push_back(a++);
        }
        if(a > 2000000) break;
    }
    int t;
    cin>>t;
    while(t--){
        long long n;
        cin>>n;

        int row = -1;
        int l, r;

        for(int i=1; i<10000; i++){ //find the row number for value of n.
            if(row!=-1) break;
            if(v[i][0]<=n && v[i].back()>=n){
                for(int j=0; j<v[i].size(); j++){
                    if(v[i][j] == n){
                        row = i;
                        l = j;
                        r = j;
                        break;
                    }
                }
            }
        }

        // calculate result.

        long long ans = 0;
        while(row>0){
            ans += getsum(v[row][l], v[row][r]);
            row--;
            l--;
            if(l<0) l=0;
            if(r>=v[row].size()) r = v[row].size()-1;
        }
       cout<<ans<<endl;
        
    }

    return 0;
}
