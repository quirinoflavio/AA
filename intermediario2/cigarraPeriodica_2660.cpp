#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll mmc(ll a, ll b) {
    return a * b / __gcd(a, b);
}

int main() {

    ll n, l, current_mmc = 1, tmp, x = 1, max_mmc, new_mmc;

    scanf("%lld %lld", &n, &l);

    for (ll i = 0; i < n; i++) {
        scanf("%lld", &tmp);
        current_mmc = mmc(tmp, current_mmc);
    }

    max_mmc = current_mmc;

    for (ll i = 1; i <= l; i++) {
        new_mmc = mmc(current_mmc, i);
        if (new_mmc > max_mmc && new_mmc <= l) {
            max_mmc = new_mmc;
            x = i;
        }
    }

    printf("%lld\n", x);

    return 0;
}