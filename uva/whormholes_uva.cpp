#include <bits/stdc++.h>

using namespace std;



struct edge
{
    int a, b, cost;
};

int n, m, v;
vector<edge> e;
const int INF = 1000000000;

bool solve()
{
    vector<int> d (n, INF);
    d[v] = 0;
    vector<int> p (n - 1);
    int x;
    for (int i=0; i<n; ++i)
    {
        x = -1;
        for (int j=0; j<m; ++j)
            if (d[e[j].a] < INF)
                if (d[e[j].b] > d[e[j].a] + e[j].cost)
                {
                    d[e[j].b] = max (-INF, d[e[j].a] + e[j].cost);
                    p[e[j].b] = e[j].a;
                    x = e[j].b;
                }
    }
    return (x == -1) ? false : true;
}

int main(){
    int q, a, b, c;
    edge ed;
    scanf("%d", &q);
    
    for(int k = 0; k < q; k++){
        scanf("%d%d", &n, &m);
        for(int i = 0; i < m; i++){
            scanf("%d%d%d", &a, &b, &c);
            ed.a = a; ed.b = b; ed.cost = c;
            e.push_back(ed);
        }
        v = 0;
        cout << ((solve()) ? "possible" : "not possible") << endl;
        e.clear();
    }
    return 0;
}