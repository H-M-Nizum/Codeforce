#include<bits/stdc++.h>
using namespace std;
int main(){
    int n, q;
    cin>>n>>q;
    vector<int> v(n);
    for(int i=0; i<n; i++){
        cin>>v[i];
    }
    // if want to use binary search stl. array must be sorted.
    sort(v.begin(), v.end());
    while (q--)
    {
        int x;
        cin>>x;
        if(binary_search(v.begin(), v.end(), x)){
            cout<<"found"<<endl;
        }
        else{
            cout<<"not found"<<endl;
        }
    }
    

    return 0;
}