#include <bits/stdc++.h>

using namespace std;


int main(){
    int n, c, s;

    while( cin >> n >> c >> s ){
        int state = 1, count = 0, e;
        for (int i = 0; i < c; i++){
            
            cin >> e;
            if (state == s) count += 1;

            if (e == -1 && state == 1) state = n;
            else if (e == 1 && state == n) state = 1;
            else state += e;

        }
        if (state == s) count += 1;
        cout << count << endl;
    }


    return 0;
}