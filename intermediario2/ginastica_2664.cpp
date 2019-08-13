#include <bits/stdc++.h>
typedef long long ll;

#define mod 1000000007
#define DIFICULDADE 100100
#define TEMPO 51

using namespace std;

ll dp[TEMPO][DIFICULDADE];

ll somaModulo(ll x, ll y)
{
    x += y;
    if (x < mod) return x;
    return x % mod;
}

ll personal(int t, int v, int d)
{
    if (t == 0)
    {
        return d >= 0 && d <= v;
    }
    if (d > v || d < 0)
        return 0;

    if (dp[t][d] != -1) return dp[t][d];

    ll res = personal(t - 1, v, d - 1);

    return dp[t][d] = somaModulo(res, personal(t - 1, v, d + 1));
}

int main()
{
    int tempo, minimo, maximo, variacao;
    ll res = 0;
    
    cin >> tempo >> minimo >> maximo;
    
    variacao = maximo - minimo;
    memset(dp, -1, sizeof dp);
    
    for (int i = 0; i <= variacao; i++)
    {
        res = somaModulo(res, personal(tempo-1, variacao, i));
    }

    cout << res << endl;

    return 0;
}