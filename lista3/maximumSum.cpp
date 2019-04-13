#include <bits/stdc++.h>

using namespace std;
int INF = 100000001;
int segTree [4000000];
int arr [1000000];


void build(int id, int l, int r){
    if (l == r) {
        segTree[id] = arr[l-1];
    }else{
        int m = (l + r) / 2;
        build(id*2, l, m);
        build(id*2+1, m+1, r);
        segTree[id] = min(segTree[id*2], segTree[id*2+1]);
    }
}

void update(int id, int l, int r, int v, int pos){
    if (l == r) segTree[id] = v;
    else{
        int m = (l + r) / 2;
        if (pos <= m) update(id*2, l, m, v, pos);
        else update(id*2+1, m+1, r, v, pos);
        segTree[id] = min(segTree[id*2], segTree[id*2+1]);
    }
}

int query(int id, int l, int r, int x, int y){
    if (x <= l && r <= y) return segTree[id];
    else if (y < l || r < x) {
        return INF;
    }
    int m = (l + r) / 2;
    return min(query(id*2, l, m, x, y), query(id*2+1, m+1, r, x, y));
}



int main(){
    
}