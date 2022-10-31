#include <bits/stdc++.h>
#define MAXN 20

using namespace std;

int bancos[MAXN];
int reservas[MAXN];

int main() {
    int b, n, d, c, v;

    scanf("%d %d", &b, &n);

    while(b != 0) {
        for(int i = 0; i < b; i++)
            scanf("%d", &reservas[i]);

        for(int i = 0; i < n; i++) {
            scanf("%d %d %d", &d, &c, &v);

            bancos[d-1] -= v;
            bancos[c-1] += v;
        }

        bool ok = true;
        for(int i = 0; i < b; i++) {
            if((bancos[i]*-1) > reservas[i]) {
                ok = false;
                break;
            }
        }

        if(ok)
            printf("S\n");
        else
            printf("N\n");

        scanf("%d %d", &b, &n);

        memset(bancos, 0, sizeof(bancos));
    }

    return 0;
}