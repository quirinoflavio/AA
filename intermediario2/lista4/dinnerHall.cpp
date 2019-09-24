#include <bits/stdc++.h>

#define MAXN 65000
using namespace std;


vector< pair<string, char> > registro;
int main(){

    int n;
    scanf("%d", &n);
    while(n != 0){
        int E = 0, i = 0;
        while(i < n){
            string hora;
            char evento;
            cin >> hora >> evento;
            registro.push_back({hora, evento});
            if (evento == 'E') E++;
            i++;
        }

        sort(registro.begin(), registro.end());
        int maxx = 0, pilha = 0;
        for(int i = 0; i < n; i++){
            if(registro[i].second == 'E'){
                pilha ++;
            } 
            else if ( registro[i].second == '?' && (n/2 - E) != 0){
                E++;
                pilha ++;
            }
            else if(registro[i].second == '?'){
                pilha--;
            }
            else {
                pilha--;
            }
            if (pilha > maxx) maxx = pilha;
        }

        cout << maxx << endl;

        scanf("%d", &n);
        registro.clear();
    }
    return 0;
}