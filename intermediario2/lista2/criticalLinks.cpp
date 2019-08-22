// RUNTIME
#include <bits/stdc++.h>

using namespace std;

#define MAXN 25000

int _count =0;
vector< pair<int, int> > _bridges;
int graph[MAXN][MAXN];

void bridgeFind(int start, bool visited[], int disc[], int low[], int parent[], int n){
    static int time = 0;
    visited[start] = true;
    disc[start] = low[start] = ++time;

    for(int v = 0; v < n; v++ ){
        if (graph[start][v] == 1){
            if(!visited[v]){
                parent[v] = start;
                bridgeFind(v, visited, disc, low, parent, n);

                low[start] = min(low[start], low[v]);
                if(low[v] > disc[start]){
                    _count++;
                    _bridges.push_back(make_pair(start, v));
                }
            }
            else if(v != parent[start]) {
                low[start] = min(low[start], disc[v]);
            }
        }
    }
}



bool bridges(int n){
    bool *vis = new bool[n];
    int *disc = new int[n];
    int *low = new int[n];
    int *parent = new int[n];

    for(int i = 0; i < n; i++){
        vis[i] = false;
        parent[i] = -1;
    }

    for(int i = 0; i < n; i++){
        if (!vis[i]) bridgeFind(i, vis, disc, low, parent, n);
    }

}



int main(int argc, char* argv[]) {
    int n, v, g, a;
    char p;
    while(cin >> n){

        for (int i = 0; i < n; i++){
            cin >> v >> p >> g >> p;
            for (int j = 0; j < g; j++){
                cin >> a;
                graph[v][a] = 1;
                graph[a][v] = 1;
            }
        }

        _bridges.clear();
        _count = 0;
        
        bridges(n);
        
        cout << _count << " critical links"<< endl;
        
        sort(_bridges.begin(), _bridges.end());
        for(int i = 0; i < _count; i++){
            cout << _bridges[i].first << " - " << _bridges[i].second << endl;
        }
        
    }
    return 0;
}