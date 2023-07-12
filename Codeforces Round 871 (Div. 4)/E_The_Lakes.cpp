#include<bits/stdc++.h>
using namespace std;

int x[1005][1005];
int vis[1005][1005];
int n, m;

vector<int>dx{1, -1, 0, 0};
vector<int>dy{0, 0, 1, -1};

int dfs(int i, int j){
    if(i<=0 || j<=0 || i>n || j>m) return 0;
    if(vis[i][j] || x[i][j] == 0) return 0;

    vis[i][j] = 1;
    int r = x[i][j];

    for(int z=0; z<=3; z++){
        r += dfs(i+dx[z], j+dy[z]);
    }
    return r;
}


int main(){
    int t;
    cin>>t;
    while(t--){
        cin>>n>>m;
        
        for(int i=1; i<=n; i++){
            for(int j=1; j<=m; j++){
                vis[i][j] = 0;
                cin>>x[i][j];
            }
            
        }
        int ans = 0;
        for(int i=1; i<=n; i++){
            for(int j=1; j<=m; j++){
                ans = max(ans, dfs(i, j));
            }
            
        }
        cout<<ans<<endl;


        
    }

    return 0;
}