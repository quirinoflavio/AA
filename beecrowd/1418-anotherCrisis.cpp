#include <bits/stdc++.h>

#define MAX (int) 1e5 + 17
using namespace std;

int T;
vector<int> graph[MAX];

int dfs(int v){
    if(graph[v].empty()) return 1;

    vector<int> lista;
    for(int i = 0; i < graph[v].size(); i++){
        int child = graph[v][i];
        lista.push_back(dfs(child));
    }
    sort(lista.begin(), lista.end());
    int qntd = (int) ceil( lista.size() * (T/100.0));
    int soma = 0;
    
    for(int i = 0; i < qntd; i++){
        soma += lista[i];
    }

    return soma; 
}


int main(){

    int n, t, e, i = 1;

    scanf("%d%d", &n, &T);
    while(n != 0){
        while(i <= n){
            scanf("%d", &e);
            graph[e].push_back(i);
            i++;
        }
        printf("%d\n", dfs(0));
        i = 1;
        for(int i = 0; i < MAX; i++) graph[i].clear();
        scanf("%d%d", &n, &T);
    }

    return 0;
}