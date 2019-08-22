#include <bits/stdc++.h>

using namespace std;

int graph[5][5] = {
   {0, 1, 1, 1, 0},
   {1, 0, 1, 0, 0},
   {1, 1, 0, 0, 0},
   {1, 0, 0, 0, 1},
   {0, 0, 0, 1, 0}
};


void bridgeFind(int start, bool visited[], int disc[], int low[], int parent[], int n){
    static int time = 0;
    visited[start] = true;
    disc[start] = low[start] = ++time;

    for(int v = 0; v < n; v++ ){
        if (graph[start][v]){
            if(!visited[v]){
                parent[v] = start;
                bridgeFind(v, visited, disc, low, parent, n);

                low[start] = min(low[start], low[v]);
                if(low[v] > disc[start]){
                    cout << start << " - " << v << endl;
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
    int count; 
    string saida = "";
    for(int i = 0; i < n; i++){
        if (!vis[i]) bridgeFind(i, vis, disc, low, parent, n);
    }

    cout << saida << " " << count << endl;

}

int main(int argc, char* argv[]) {

    bridges(5);
    return 0;
}