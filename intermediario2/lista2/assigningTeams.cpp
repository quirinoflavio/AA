#include <bits/stdc++.h>

using namespace std;

int main(){
    int A, B, C, D;

    while(cin >> A >> B >> C >> D){

        int menor =  min(abs((A + D) - (B+C)),  min( abs((A + B) - (C+D)), abs((A + C) - (B+D)) ));

        cout << menor << endl;
    }
    return 0;
}