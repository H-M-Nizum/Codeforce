#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n, m;
        cin>>n>>m;
        int frq[n+1] ={0};
        set<int>s;
        for(int i=1; i<=m; i++){
            int u, v;
            cin>>u>>v;
            frq[u]++;
            frq[v]++;

        }
        for(int i:frq){
            s.insert(i);

        }
       
        s.erase(s.find(0));
        int len = s.size();
        if(len == 3){
            auto it = s.begin();
            advance(it,1);
            int c = 0;
            for(int i:frq){
                if(*it == i) c++; 
            }
            if(c == 1){
                cout<<*it<<" ";
                auto jt = s.begin();
                advance(jt,2);
                cout<<*jt - 1<<endl;
            }
            else{
                auto jt = s.begin();
                advance(jt,2);
                cout<<*jt<<" "<<*it-1<<endl;
            }
        }
        else if(len == 2){
            auto jt = s.begin();
            advance(jt,1);
            cout<<*jt<<" "<<*jt - 1<<endl;
        }
       

        
    }

    return 0;
}
