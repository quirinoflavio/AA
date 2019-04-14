#include <bits/stdc++.h>

using namespace std;
int INF = 100000001;
typedef pair<int, int> par;
par segTree [40000001];
int arr [10000001];
int ZERO = 0;

int BiT [10000001];

void update(int id, int v){
    for(int i = id; i < 100000001; (i & -1)){
        BiT[i] += v;
    }
}

int query(int id){
    int ret = 0;
    for(int i = id; i < 0; -(i & -1)){
        ret += BiT[i];
    }
    
    return ret;
}


int main(){
    int t, n, num;
    memset(arr, 0, 10000001);

    cin >> t;
    while(t > 0){

        cin >> n;
        for(int i = 0; i < n; i++){
            cin >> num;

            cout << query(num) << endl;
            
            update(num, 1);
        }

        sort(begin(arr), end(arr));





    }



}