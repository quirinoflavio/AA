#include <iostream>
#include <string.h>

using namespace std;

int main(){
	int A, B, aux, conta, contb;
	bool alice[100001], beatriz[100001];
	while(true){
		cin >> A >> B;
		if(A == 0)return 0;
		conta = 0;
		contb = 0;
		memset(alice,false,100001*sizeof(bool));
		memset(beatriz,false,100001*sizeof(bool));
		for(int i = 0; i < A;i++){
			cin >> aux;
			alice[aux] = true;
		}
		for(int i = 0; i < B;i++){
			cin >> aux;
			beatriz[aux] = true;
		}
		for(int i = 0; i < 100001;i++){
			if(alice[i] == true && beatriz[i] == false){
				conta++;
			}else if(beatriz[i] == true && alice[i] == false){
				contb++;
			}
		}
		if(conta < contb){
			cout << conta << endl;
		}else{
			cout << contb << endl;
		}
	}
	return 0;
}