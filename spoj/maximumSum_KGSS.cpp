#include <bits/stdc++.h>

using namespace std;
int INF = 100000001;
typedef pair<int, int> par;
par segTree [4000000];
int arr [100000];
int ZERO = 0;

par getPair(pair<int, int> p1, pair<int, int> p2){
    int pm, sm, n;
    int elements[] = {p1.first, p1.second, p2.first, p2.second};
    n = sizeof(arr)/sizeof(arr[0]);
    sort(begin(elements), end(elements));
    pm = elements[3];
    sm = elements[2];
    //cout << p1.first << " " << p1.second << " - " << p2.first << " " << p2.second << " - " << pm << " " << sm << endl;
    return par(pm, sm);
}

void build(int id, int l, int r){
    if (l == r) segTree[id] = par(arr[l-1], 0);
    else {
        int m = (l + r) / 2;
        build(id*2, l, m);
        build(id*2+1, m+1, r);
        segTree[id] = getPair(segTree[id*2], segTree[id*2+1]);
    }
}
void update(int id, int l, int r, int v, int pos){
    if (l == r) segTree[id] = par(v, 0);
    else{
        int m = (l + r) / 2;
        if (pos <= m) update(id*2, l, m, v, pos);
        else update(id*2+1, m+1, r, v, pos);
        segTree[id] = getPair(segTree[id*2], segTree[id*2+1]);
    }
}

par query(int id, int l, int r, int x, int y){
    if (x <= l && r <= y) return segTree[id];
    else if (y < l || r < x) {
        return par(0,0);
    }
    int m = (l + r) / 2;
    return getPair(query(id*2, l, m, x, y), query(id*2+1, m+1, r, x, y));
}
int main(){
    int arrSize, q, i, x, sum;
    char op;
    par p;

    cin >> arrSize;
    for(int i = 0; i < arrSize; i++){
        cin >> arr[i];
    }
    build(1, 1, arrSize);
    cin >> q;
    for(int j = 0; j < q; j++){
        cin >> op >> i >> x;
        if (op == 'U') update(1, 1, arrSize, x, i);
        
        else {
            p = query(1, 1, arrSize, i, x);
            sum = p.first + p.second;
            cout << sum << endl;
        }
    }



}