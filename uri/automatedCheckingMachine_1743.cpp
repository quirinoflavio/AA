#include<bits/stdc++.h>

using namespace std;

int p1, p2, p3, p4, p5, o1, o2, o3, o4, o5;

int main(){

    while(cin >> p1 >> p2 >> p3 >> p4 >> p5){
        cin >> o1 >> o2 >> o3 >> o4 >> o5;
        if (p1^o1 && p2^o2 && p3^o3 && p4^o4 && p5^o5)
            cout << "Y" << endl;
        else
            cout << "N" << endl;
        
    }

    return 0;
}