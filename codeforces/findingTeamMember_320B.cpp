#include <bits/stdc++.h>
 
using namespace std;
 
int matriz[805][805] = {0};
int team[805] = {0};
 
int main () {
 int n ;
	cin >> n;
	for (int i = 2; i <= (2*n); i++) {
		for (int j = 1; j < i; j++) {
			cin >> matriz[i][j];
		}
	}
	int times = n;
	while (times--) {
		int tempi = 0, tempj = 0, maxi = INT_MIN;
		for (int i = 2; i <= (2*n); i++) {
			for (int j = 1; j < i; j++) {
				if (matriz[i][j] > maxi) {
					maxi = matriz[i][j];
					tempi = i;
					tempj = j;
				}
			}
		}
		for (int i = 1; i <= (2*n); i++) {
			matriz[tempi][i] = 0;
			matriz[tempj][i] = 0;
			matriz[i][tempj] = 0;
			matriz[i][tempi] = 0;
		}
		team[tempi] = tempj;
		team[tempj] = tempi;
	}
	for (int i = 1; i <= (2*n); i++) {
		cout << team[i];
		if (i == 2*n) {
			cout << endl;
		} else {
			cout << " ";
		}
	}
	return 0;
}