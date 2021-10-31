#include <bits/stdc++.h>
#define MAXN 10000

using namespace std;

int pessoas[MAXN];

int main() {
    int n, r, tmp;

    while(scanf("%d %d", &n, &r) != EOF) {
        memset(pessoas, -1, sizeof(pessoas));

        for(int i = 0; i < r; i++) {
            scanf("%d", &tmp);

            pessoas[tmp-1] = 0;
        }

        string res = "";
        for(int i = 0; i < n; i++) {
            if(pessoas[i] == -1)
                res += to_string(i+1)  + " ";
        }

        if(res == "")
            printf("*\n");
        else
            cout << res << endl;
    }

    return 0;
}