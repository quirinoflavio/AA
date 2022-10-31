#include <bits/stdc++.h>

#define MAX 100001
using namespace std;
 
bitset<MAX> vis;
vector<int> graph[MAX];
vector< pair<int, int> > bridges;
int sz, n, q, ans, num[MAX], parent[MAX], low[MAX];

void dfs(int no){
    vis[no] = true;
    num[no] = low[no] = sz++;
    for(int i = 0; i < graph[no].size(); i++){
        int child = graph[no][i];
        if(!vis[child]){
            parent[child] = no;
            dfs(child);
            if(low[child] > num[no]) {
                ans++; 
                bridges.push_back({min(no, child), max(child, no)});
            }
            low[no] = min(low[no], low[child]);
        }else if(child != parent[no]) low[no] = min(low[no], num[child]);
    }
}
 
void ponte(int tam){
    sz = 0;
    ans = 0;
    vis.reset();
    memset(low, -1, sizeof low);
    memset(num, -1, sizeof num);
    memset(parent, -1, sizeof parent);
    dfs(0);

    for(int i = 0; i < tam; i++){
        if (!vis[i]) dfs(i);
    }
}

int main(){
    while(cin >> n){
        for(int i = 0; i <= n; i++){
            graph[i].clear();
        }

        for(int i = 0; i < n; i++){

            int v, g, a;
            char p; 

            cin >> v >> p >> g >> p;
            for(int j = 0; j < g; j++){
                cin >> a;
                graph[v].push_back(a);
            }
            
        }

        ponte(n);

        cout << ans << " critical links" << endl;

        sort(bridges.begin(), bridges.end());
        for(int i = 0; i < ans; i++){
            cout << bridges[i].first << " - " << bridges[i].second << endl;
        }
        bridges.clear();

        cout << endl;

    }
    return 0;
}