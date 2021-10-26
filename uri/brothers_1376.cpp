#include <bits/stdc++.h>

#define MAX 101
using namespace std;

int mun[MAX][MAX][MAX];
int N;


void guerra(int k, int R, int C){
    for(int x = 0; x < R; x++){
            for(int y = 0; y < C; y++){
                bool changed = false;
                if(x-1 >= 0 &&  (mun[k][x-1][y] + 1) % N == mun[k][x][y]){
                    mun[k+1][x][y] = mun[k][x-1][y];
                    changed = true;
                }
                if(x+1 < R && (mun[k][x+1][y] + 1) % N == mun[k][x][y]){
                    mun[k+1][x][y] = mun[k][x+1][y]; 
                    changed = true;
                }
                if(y-1 >= 0 && (mun[k][x][y-1] + 1) % N == mun[k][x][y]){
                    mun[k+1][x][y] = mun[k][x][y-1]; 
                    changed = true;
                } 
                if(y+1 < C && (mun[k][x][y+1] + 1) % N == mun[k][x][y]){ 
                    mun[k+1][x][y] = mun[k][x][y+1];
                    changed = true; 
                }
                if(!changed) mun[k+1][x][y] = mun[k][x][y];
            }
        }
}

int main(){

    int R, C, K;

    scanf("%d%d%d%d", &N, &R, &C, &K);
    while(N != 0){
        for(int i = 0; i < R; i++){
            for(int j = 0; j < C; j++){
                scanf("%d", &mun[0][i][j]);
            }
        }
        
        for(int i = 0; i < K; i++){
            guerra(i, R, C);
        }
        for(int p = 0; p < R; p++){
            for(int l = 0; l < C; l++){
                cout << mun[K][p][l] << ((l < (C - 1) ? " " : ""));
            }
            printf("\n");
        }
        scanf("%d%d%d%d", &N, &R, &C, &K);
    }    

    return 0;
}