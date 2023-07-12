#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n, m;
        cin>>n>>m;
        queue<int> q;
        if(n==m){
            cout<<"YES"<<endl;
            continue;
        }
        else if(n%3 == 0){
            int x = n/3;
            q.push(x);
            q.push(n-x);
        }
        else{
            cout<<"NO"<<endl;
            continue;;
        }
        int ans = 0;
        while(!q.empty()){
            int f = q.front();
            q.pop();
            if(f == m){
                ans = 1;
                break;
            }
            else if(f > m && f%3 == 0){
                int x = f/3;
                q.push(x);
                q.push(f-x);
            }
        }
        if(ans == 1) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
       
        
    }

    return 0;
}

//################################
//#####   use recoursion     #####
// ###############################

// int solve(int n, int m){
//     if(n==m) return 1;
//     if(m>n) return 0;

//     if(n%3 == 0) return solve(n/3, m) | solve(2*n/3, m);
//     return 0;
// }

// #include<bits/stdc++.h>
// using namespace std;
// int main(){
//     int t;
//     cin>>t;
//     while(t--){
//         int n, m;
//         cin>>n>>m;

//         if(solve(n, m)) cout<<"YES"<<endl;
//         else cout<<"NO"<<endl;
        
//     }

//     return 0;
// }