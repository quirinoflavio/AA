#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll prime(ll n)
{
    if(n%2 == 0) n--;

    for(int i = n; i >= 2; i-=2){
        bool b = false;
        
        for(int j = 3; j <= ceil(sqrt(i)); j+=2){
            
            if(i%j == 0 || i%2==0){
                b = true;
                break;
            }

        }

        if(!b) return i;

    }
}
    int main()
    {

        ll n;
        while(cin >> n){

            cout << ( (n==2) ? 2 : prime(n)) << endl;

        }
        return 0;
    }