#include <bits/stdc++.h>
#define MAXN 3

using namespace std;

int main() {
    int n, l, c;
    string aux;

    while(scanf("%d %d %d", &n, &l, &c) != EOF) {
        int qp = 0, qc = 0, res = 1;

        for(int i = 0; i < n; i++) {
            cin >> aux;

            if(qc == 0)
                qc += aux.length();
            else {
                if((qc + 1 + aux.length()) > c) {
                    qc = aux.length();
                    if((qp + 1) >= l) {
                        qp = 0;
                        res++;
                    } else
                        qp++;
                } else
                    qc += (1 + aux.length());
            }
        }

        printf("%d\n", res);
    }

    return 0;
}