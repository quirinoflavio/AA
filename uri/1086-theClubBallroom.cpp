#include <bits/stdc++.h>

using namespace std;

int main(){
    int M, N;
    while(true){
        cin >> M >> N;
        if(N + M == 0)break;
        int L, K;
        M*=100;
        N*=100;
        cin >> L >> K;
        int tabuas[K];
        int tenhoTabuas = 0;
        for(int i = 0; i < K; i++){
            cin >> tabuas[i];
            tabuas[i]*=100;
            if(tabuas[i] == M)tenhoTabuas++;
        }
        sort(tabuas,tabuas+K);
        int duasTabuas = 0;
        int ini = 0, fim = K - 1;
        for(int i = ini; i <= fim; i++){
            for(int j = fim; j > ini; j--){
                if(tabuas[i]+tabuas[j] == M){
                    duasTabuas++;
                    fim = j - 1;
                    ini++;
                    break;
                }
            }
        }
        int resp = 1e9;
        if(N%L == 0 && N <= (tenhoTabuas+duasTabuas)*L){
            int usadas = N/L;
            if(tenhoTabuas < usadas)tenhoTabuas += (usadas - tenhoTabuas)*2;
            else if(tenhoTabuas > usadas)tenhoTabuas = usadas;
            resp = min(resp,tenhoTabuas);
        }
        tenhoTabuas = 0;
        duasTabuas = 0;
        ini = 0;fim = K - 1;
        for(int i = 0; i < K; i++){
            if(tabuas[i] == N)tenhoTabuas++;
        }
        for(int i = ini; i <= fim; i++){
            for(int j = fim; j > ini; j--){
                if(tabuas[i]+tabuas[j] == N){
                    duasTabuas++;
                    fim = j - 1;
                    ini++;
                    break;
                }
            }
        }
        if(M%L == 0 && M <= (tenhoTabuas+duasTabuas)*L){
            int usadas = M/L;
            if(tenhoTabuas < usadas)tenhoTabuas += (usadas - tenhoTabuas)*2;
            else if(tenhoTabuas > usadas)tenhoTabuas = usadas;
            resp = min(resp,tenhoTabuas);
        }
        if(resp == 1e9)cout << "impossivel\n";
        else cout << resp << endl;
    }
    return 0;
}