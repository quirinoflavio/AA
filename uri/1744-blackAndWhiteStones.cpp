#include<bits/stdc++.h>

using namespace std;

#define ll long long

ll c, r;
string stones;

int main(){

    while (cin >> c >> r){
        
        cin >> stones;

        ll i = 0, j = stones.size()-1, k, cw = 0, ct = 0;

        while(1){
            while(i < j && stones[i] != 'W') i++;
            while(j > i && stones[j] != 'B') j--;
            
            if (i < j){
                cw = j-i;
                ct += min(cw * (c-r), c);
                i++;
                j--;
                cw = 0;
            }
            else break;
        }

        cout << ct << endl;
    }    



    return 0;
}