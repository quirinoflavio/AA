#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, a, b, r;

    while(1){
        a = 0;
        b = 0;
        cin >> n;
        if (n == 0) break;
        for(int i = 0; i < n; i++){
            cin >> r;
            if (r == 1) b++;
            else a++;
        }
        printf("Mary won %d times and John won %d times\n", a, b);
        

    }

    return 0;
}