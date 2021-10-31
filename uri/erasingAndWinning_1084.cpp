#include <bits/stdc++.h>

using namespace std;

int main(){
    while(true){
        string nome;
        deque < char > pilha;
        int N, M;
        cin >> N >> M;
        if(!(N || M))return 0;
        cin >> nome;
        int m = M;
        pilha.push_back(nome[0]);
        for(int i = 1; i < nome.size(); i++){
            while(!pilha.empty() && nome[i] > pilha.back() && M){
                pilha.pop_back();
                M--;
            }
            pilha.push_back(nome[i]);
        }
        for(int i = 0; i < N-m; i++){
            cout << pilha[i];
        }
        cout << endl;
        pilha.clear();
    }
    return 0;
}