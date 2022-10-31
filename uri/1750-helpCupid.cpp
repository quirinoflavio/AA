#include<bits/stdc++.h>

#define MAXN 1000

using namespace std;

int numeros[MAXN];

int main(){
    int n, num, acum1, acum2;
    while(cin >> n){
        for(int i = 0; i < n; i++){
            scanf("%d", &numeros[i]);
        }

        sort(numeros, numeros+n);

        acum1 = 0;
        for(int i = 0; i < n; i+=2){
            acum1 += min(abs(numeros[i] - numeros[i+1]), 24 - abs(numeros[i] - numeros[i+1]));  
        }

        acum2 = 0;
        acum2 += min(abs(numeros[0] - numeros[n-1]), 24 - abs(numeros[0] - numeros[n-1]));
        for(int i = 1; i < n-1; i+=2){
            acum2 += min(abs(numeros[i] - numeros[i+1]), 24 - abs(numeros[i] - numeros[i+1]));  
        }

        printf("%d\n", min(acum1, acum2));
    }
    return 0;
}