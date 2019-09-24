#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> pii;

vector <pii> pontos;
long long dist, xx, yy;
unordered_map<long long, long long> d2;

int main(){
    int n, x, y;
    scanf("%d", &n);
    
    while(n!=0){
        
        long long cont = 0;

        for(int i = 0; i < n; i++) {
            scanf("%d%d", &x, &y);
            pontos.push_back({x, y});
        }

        for(int i = 0; i < n; i++){
            d2.clear();
            
            for(int j = 0; j < n; j++){
                if(i != j){
                    xx = pontos[i].first - pontos[j].first;
                    yy = pontos[i].second - pontos[j].second;
                    dist = pow(xx, 2) + pow(yy, 2);
                    d2[dist]++;
                }
            }

            for (auto& p: d2) {
                cont += (p.second * (p.second-1)) / 2; 
            }
        }

        cout << cont << endl;

        scanf("%d", &n);
        pontos.clear();
    }



    return 0;
}