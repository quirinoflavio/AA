// INCOMPLETE
#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int ca(int x1, int y1, int x2, int y2){
    int m;
    
    if ((x2 - x1) == 0) m = 0;
    else m = (y2 - y1) / (x2 - x1);
    
    return m;
}

int abaixo(int m, int x1, int y1, int Px){
    int y = m * (x1 - Px);
    return y < y1;
}

int main(){
    vector<pair<int, int>> pontos;
    int n, A, B, x, y, x1, y1, cont, quant = 0;
    cin >> n >> A >> B;

    for (int i = 0; i < n; i++){
        cin >> x >> y;
        pontos.push_back(make_pair(x, y));
    }

    for (int i = 0; i < n; i++){
        x = pontos[i].first;
        y = pontos[i].second;
        cont = 0;
        int mA = ca(A, 0, x, y);
        int mB = ca(B, 0, x, y);
        cout << " ##   " << x << " " << y  << "  ###"<< endl;
        for (int j = 0; j < n; j++){
            x1 = pontos[j].first;
            y1 = pontos[j].second;

            if (i != j) {
                cout << x1 << " " << y1 << " " << (abaixo(mA, x1, y1, A) && abaixo(mB, x1, y1, B)) << endl;
                if (abaixo(mA, x1, y1, A) && abaixo(mB, x1, y1, B)) cont++;
            }
        }

        if (cont > quant) quant = cont;
        cont = 0;
    }
    cout << quant << endl;
    return 0;
}
