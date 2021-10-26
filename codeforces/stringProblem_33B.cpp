#include <bits/stdc++.h>

#define N 26
#define inf 100000000
#define A 'a'
#define loop(x,n) for(int x = 0; x < n; ++x)

using namespace std;

int dist[N][N];

int main() {
    
    int i, j, k, n, c, mn;

    loop(i, N){
        loop(j, N){
            if (i != j) dist[i][j] = inf;
            else dist[i][j] = 0;
        }
    }

    string s, t;
    cin >> s >> t;

    if(s.length() != t.length()){
        cout << -1 << endl;
        return 0;
    }

    cin >> n;
    char v1, v2, v3;

    while(n--){
        cin >> v1 >> v2 >> c;
        dist[v1-A][v2-A] = min(dist[v1-A][v2-A], c);
    }

    loop(k, N){
        loop(i, N){
            loop(j, N){
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j]);
            }
        }
    }

    int cost = 0;
    n = s.length();
    
    loop(i, n) {
        if (s[i] != t[i]){
            mn = inf;
            loop(j, N){
                c = dist[s[i]-A][j] + dist[t[i]-A][j];
                if (c < mn) {
                    v3 = j + A; 
                    mn = c;
                }
            }

            cost += mn;
            s[i] = t[i] = v3;
            
            if (mn >= inf) {
                cout << -1 << endl;
                return 0;
            }
        }
    }
    

    cout << cost << endl;
    cout << s << endl;

    return 0;
}