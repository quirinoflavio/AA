#include <bits/stdc++.h>

#define MAXN (int) 1e4 + 1
#define INF (int) 1e7
using namespace std;

vector<int> notas[MAXN];
int tam[MAXN];
int queries, divs, qntd, nota, pos, acum, mindif;
int main(){
    
    scanf("%d", &divs);
    while(divs != 0){
        memset(tam, 0, MAXN);
        
        
        for (int i = 0; i < divs; i++){
            scanf("%d", &qntd);
            tam[i] = qntd;
            notas[i].clear();
            for(int j = 0; j < qntd; j++){
                scanf("%d", &nota);
                notas[i].push_back(nota);

            }
            sort(notas[i].begin(), notas[i].end());
        }

        acum = 0;
        mindif = INF;
        for(int tz = 0; tz <= 1000; tz++){
            for (int i = 0; i < divs; i++){        
                    pos = lower_bound(notas[i].begin(), notas[i].end(), tz) - notas[i].begin();
                    if(pos == 0 || pos == tam[i]) acum += tam[i];    
                    else acum += abs( (pos) - (tam[i] - pos) );
                   
            }
            if (acum < mindif) mindif = acum;
            acum = 0;

        }

        printf("%d\n", mindif);
        scanf("%d", &divs);

    }
    

    return 0;
}