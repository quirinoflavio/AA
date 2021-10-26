//WA
#include <bits/stdc++.h>

using namespace std;
int INF = 100000001;
typedef pair<int, int> par;
int segTree [8000001];
par arr [2000001];
int ZERO = 0;

par BiT [10000001];

bool compare(par p1, par p2){
    return p1.first > p2.first;
}


void insert(int id, int l, int r, int index){
    if(index < l || index > r) return;
    if (l == r && r == index){ 
        segTree[id] += 1;
        return;
    }
    
    int m = (l + r) / 2;
    insert(id*2, l, m, index);
    insert(id*2+1, m+1, r, index);
    segTree[id] = segTree[id*2] + segTree[id*2+1];
}

void update(int id, int l, int r, int v, int pos){
    if (l == r) segTree[id] += v;
    else{
        int m = (l + r) / 2;
        if (pos <= m) update(id*2, l, m, v, pos);
        else update(id*2+1, m+1, r, v, pos);
        segTree[id] = segTree[id*2] + segTree[id*2+1];
    }
}

int query(int id, int l, int r, int x, int y){
    if (x <= l && r <= y) return segTree[id];
    else if (y < l || r < x) {
        return 0;
    }
    int m = (l + r) / 2;
    return query(id*2, l, m, x, y) + query(id*2+1, m+1, r, x, y);
}


int main(){
    int t, n, num, soma;
    
    cin >> t;
    while(t > 0){
        memset(segTree, 0, 8000001);
        soma = 0;
        cin >> n;
        for(int i = 1; i <= n; i++){
            cin >> num;
            arr[i] = par(num, i);
        }
        sort(begin(arr), end(arr), compare);

        for (int i = 0; i < n; i++){
            soma += query(1, 1, n, 1, arr[i].second);
            update(1, 1, n, 1, arr[i].first);
        }
        cout << soma << endl;


        t--;
     
    }


}