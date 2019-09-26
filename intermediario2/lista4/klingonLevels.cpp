#include <bits/stdc++.h>

#define MAXN (int) 1e4 + 1

using namespace std;

vector<int> notas[MAXN];
int tam[MAXN];

int main(){
    int queries, divs, qntd, nota, t=0, pos, acum;
    scanf("%d", &divs);
    while(divs != 0){
        
        for (int i = 0; i < divs; i++){
            scanf("%d", &qntd);
            tam[i] = qntd;
            for(int j = 0; j < qntd; j++){
                scanf("%d", &nota);
                notas[i].push_back(nota);

            }
            sort(notas[i].begin(), notas[i].end());
        }

        t = 0;
        acum = 0;
        for(int tz = )
        for (int i = 0; i < divs; i++){        
            for(int j = 0; j < qntd; j++){
                pos = lower_bound(notas[i].begin(), notas[i].end(), t) - notas[i].begin();
                if(notas[i][pos] == t){
                    pos--;
                }
                acum += abs( (pos+1) - (pos+1 - tam[i]) );
                
                //1 2 2 3 3 3 4 5
                //0 1 2 3 4 5 6 7
            }
        }

        printf("%d\n", acum);
        scanf("%d", &divs);

    }
    

    return 0;
}