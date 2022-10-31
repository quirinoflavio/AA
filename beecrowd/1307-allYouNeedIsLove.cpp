#include <bits/stdc++.h>

using namespace std;

int main(){

    int n, a, b, i = 0, c;
    string sa, sb;
    scanf("%d", &n);

    while(i < n){
        cin >> sa;
        cin >> sb;
        a = stoi(sa, nullptr, 2);
        b = stoi(sb, nullptr, 2);
        c = __gcd(a, b);
        if(c > 1) printf("Pair #%d: All you need is love!\n", i+1);
        else printf("Pair #%d: Love is not all you need!\n", i+1);
        i++;
    }


    return 0;
}