#include <bits/stdc++.h>

using namespace std;

int main() {
    int j, r, n = 0, maxx = -1, res;

    scanf("%d %d", &j, &r);

    int jgs[j], l[j*r];

    memset(jgs, 0, sizeof(jgs));

    for (int i = 0; i < (j*r); i++)
        scanf("%d", &l[i]);

    for (int i = 0; i < r; i++) {
        for (int k = 0; k < j; k++) {
            jgs[k] += l[n];
            n++;
        }
    }

    for (int i = (j-1); i >= 0; i--) {
        if (jgs[i] > maxx) {
            res = i;
            maxx = jgs[i];
        }
    }

    printf("%d\n", res+1);

    return 0;
}