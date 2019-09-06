#include <bits/stdc++.h>
#define MAXN 100000

using namespace std;

int elementos[MAXN];
int linhas[MAXN];

int main() {
    int n, m;

    scanf("%d%d", &n, &m);

    while(n != 0) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++)
                scanf("%d", &elementos[j]);
            if(m > 1)
                elementos[m-2] = max(elementos[m-2], elementos[m-1]);
            for (int j = (m-3); j >= 0; j--)
                elementos[j] = max(elementos[j+1], (elementos[j] + elementos[j+2]));
            linhas[i] = elementos[0];
        }

        if(n > 1)
            linhas[n-2] = max(linhas[n-2], linhas[n-1]);
        for (int i = (n-3); i >= 0; i--)
            linhas[i] = max(linhas[i+1], (linhas[i] + linhas[i+2]));

        printf("%d\n", linhas[0]);
        scanf("%d %d", &n, &m);
    }

    return 0;
}