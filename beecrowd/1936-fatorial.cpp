#include <bits/stdc++.h>

using namespace std;

int l[] = {1, 2, 6, 24, 120, 720, 5040, 40320, 362880};

int main() {
    int n, i, res = 0;

    scanf("%d", &n);

    while (n > 0) {
        i = 0;

        while (n >= l[i])
            i++;
        
        n -= l[i-1];
        res++;
    }

    printf("%d\n", res);

    return 0;
}