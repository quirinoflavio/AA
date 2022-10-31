#include <bits/stdc++.h>

#define ll long long

using namespace std;
int q[101];

int main(){

    q[0] = 0;
    for (int i = 1; i <= 101; i ++){
        q[i] = pow(i, 2) + q[i-1];
    }

    ll n;
    cin >> n;
    while(n != 0){
        cout << q[n] << endl;
        cin >> n;
        
    }
    

    return 0;
}